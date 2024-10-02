#!/usr/bin/env python
import os
import subprocess
import glob
import sys
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import requests

load_dotenv()

help_guide = """
To get more information write "passive --help" or "passive -h"
"""

help_string = """
Welcome to passive v1.0.0

OPTIONS:
    -fn         Search with full-name
    -ip         Search with ip address
    -u          Search with username
"""

fn_format = """
Welcome to passive v1.0.0

OPTION:
    -fn         Search with full-name

EXAMPLE:
    passive -fn "first_name last_name"
"""
ip_format = """
Welcome to passive v1.0.0

OPTION:
    -ip         Search with ip address

EXAMPLE:
    passive -ip 123.123.123.123
"""
u_format = """
Welcome to passive v1.0.0

OPTION:
    -u          Search with username

EXAMPLE:
    passive -u "username"
"""


def write_to_file(text, filename, log_bool=True):
    """Writes the given text to the specified file."""
    try:
        with open(filename, 'a') as file:  # Open file in append mode
            file.write(text + '\n')  # Write text followed by a newline
        if bool:
            print(f"Saved in {filename}")
    except Exception as e:
        if bool:
            print(f"An error occurred while writing to the file: {e}")


def return_index():
    result_files = glob.glob("result*.txt")
    i = len(result_files)  # Set i to the next available index

    if i == 0:
        i = ""
    return i


def main():
    arguments = sys.argv[1::]
    print("ARGUMENTS >>>", arguments)
    try:
        arg1 = arguments[0]
        match arg1:
            case "-h":
                print(help_string)
            case "--help":
                print(help_string)
            case "-fn":
                try:
                    arg2 = arguments[1]
                    fn(arg2)
                except:
                    print(fn_format)
            case "-ip":
                try:
                    arg2 = arguments[1]
                    ip(arg2)
                except:
                    print(ip_format)
            case "-u":
                try:
                    arg2 = arguments[1]
                    user(arg2)
                except:
                    print(u_format)
            case _:
                print(help_guide)

    except:
        print(help_guide)


def run_sherlock(username):
    i = return_index()
    try:
        # Prepare the command to run Sherlock with specified sites
        command = [
            'sherlock',
            '--site', 'twitter',
            '--site', 'linkedin',
            '--site', 'instagram',
            '--site', 'twitch',
            '--site', 'tryhackme',
            '--output', f"result{i}.txt",
            '--print-all',
            username
        ]

        # Run Sherlock and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if the process completed successfully
        if result.returncode != 0:
            print(f"Error running Sherlock: {result.stderr.strip()}")
            return None

        # Return the output from the command
        return result.stdout.strip()  # Return cleaned output
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def find_fullName(fullName: str):
    result_index = return_index()
    # Split the fullName into first and last names and join them with '+'
    query_name = '+'.join(fullName.split())
    url = f"https://www.118000.fr/search?who={query_name}"

    # request the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    names = []
    for stuff in soup.find_all('h2', class_="name")[4::]:
        names.append(stuff.find('a').decode_contents())
    addresses = []
    for stuff in soup.find_all('div', class_="h4")[4::]:
        addresses.append("\n".join((stuff.decode_contents()).split("<br/>")))
    out = []

    for i in range(0, names.__len__()):
        text = f"""Searched name: {fullName}
Full name: {names[i]}
Address: {addresses[i]}"""
        out.append(text)

        if i < 3:
            print(text)
            write_to_file(text, f"result{result_index}.txt")
            print()
        elif i == 3:
            print("Total results:", names.__len__())
            write_to_file(text, f"result{result_index}.txt", False)
    return out


def lookup_ip(ip):
    url = f"https://api.ip2location.io/?key={os.getenv('IP_API_KEY')}&ip={ip}"
    response = requests.get(url)
    data = response.json()
    return data


def fn(full_name):
    find_fullName("Jean Dupont")
    return


def ip(ip):
    i = return_index()
    data = lookup_ip(ip)
    try:
        isp = data["as"]
        lat = data["latitude"]
        lon = data["longitude"]
        print(f"ISP: {isp}")
        print(f"City Lat/Lon:   ({lat}) / ({lon})")
        write_to_file(f"""IP: {ip}
ISP: {isp}
City Lat/Lon:   ({lat}) / ({lon})""", f"result{i}.txt")

        return
    except Exception as e:
        print(f"An error occurred: {e}")


def user(username):
    text = run_sherlock(username)
    if type(text) is str:
        print(text)
    return


main()

#!/usr/bin/env python
import sys

print("Hello World!")

help_guide = """
To get more information write "passive --help"
"""

help_string = """
Welcome to passive v1.0.0

OPTIONS:
    -fn         Search with full-name
    -ip         Search with ip address
    -u          Search with username
"""


def main():
    arguments = sys.argv[1::]
    try:
        arg1 = arguments[0]
        match arg1:
            case "-h":
                print(help_string)
            case "--help":
                print(help_string)
            case "-fn":
                print("fn")
            case "-ip":
                print("ip")
            case "-u":
                print("u")
            case _:
                print(help_string)

        print(arguments)
    except:
        print("Exception occured")


main()

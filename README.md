# Passive Recon Tool - `passive`

## Introduction

`passive` is an open-source reconnaissance tool designed for passive information gathering during cybersecurity exercises. This tool allows users to search for specific details based on a full name, IP address, or username. The tool leverages public directories and services to gather information without direct interaction with the target, making it a powerful passive reconnaissance tool.

The tool can:
- Retrieve a phone number and address when searching by full name.
- Display the Internet Service Provider (ISP) and location (latitude/longitude) for a given IP address.
- Check for a username's existence on at least 5 known social media platforms.

This project is designed for educational purposes only. It demonstrates how open-source intelligence (OSINT) techniques can be used in cybersecurity assessments.

## Features

- Search using a full name, IP address, or username.
- Results are saved in text files for each query.
- Provides insights into basic passive OSINT methods.
- Supports customizable API integrations for enhanced data gathering (Bonus feature).

## Installation

Clone the repository and navigate to the project directory:

```bash
$ git clone https://01.kood.tech/git/mkuzmina/passive
$ cd passive
```

Ensure you have all the required libraries installed for the programming language you used (e.g., Python dependencies).

For Python (if used):
```bash
$ pip install -r requirements.txt
```
To test the ip address you will have to get your own api key from api.ip2location.io! (Key name: IP_API_KEY should be in .env)

## Usage

Run the program using the following commands:

```bash
$ passive --help
```

This will display the help menu with available options.

### Options

- **Full Name Search**: Search by full name to retrieve the person's address and phone number.

  ```bash
  $ passive -fn "Jean Dupont"
  ```

  **Output Example:**

  ```bash
  First name: Jean
  Last name: Dupont
  Address: 7 rue du Progrès, 75016 Paris
  Saved in result.txt

  ...
  ```

- **IP Address Search**: Search by IP to retrieve the city and Internet Service Provider (ISP) information.

  ```bash
  $ passive -ip 91.191.77.90
  ```

  **Output Example:**

  ```bash
  ISP: O2 Czech Republic A.S.
  City Lat/Lon:   (48.14821) / (17.10696)
  Saved in result12.txt
  ```

- **Username Search**: Search for a username and check if it is registered on at least 5 social media platforms.

  ```bash
  $ passive -u "@user01"
  ```

  **Output Example:**

  ```bash
  [*] Checking username @user01 on:
  
  [-] LinkedIn: Illegal Username Format For This Site!
  [-] Twitter: Error Connecting 
  [-] Instagram: Not Found!
  [-] Twitch: Not Found!
  [+] TryHackMe: https://tryhackme.com/p/@user01
  
  [*] Search completed with 1 results
  ```

### Saving Results

Each search result will be saved in a text file:
- First result is saved in `result.txt`
- Second result is saved in `result2.txt`
- Subsequent results are saved in sequentially numbered result files.

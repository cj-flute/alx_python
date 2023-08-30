#!/usr/bin/python3

"""
    A python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""

import requests
import sys


def main():
    """
        The main function
        Takes your username and password
        use basic authentication
    """
    username = argv.sys[1]
    password = argv.sys[2]
    url = 'https://github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_response = response.json()
    print(json_response.get("id"))
    pass


if __name__ == "__main__":
    main()

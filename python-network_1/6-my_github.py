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
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    url = 'https://api.github.com/user'
    data = (username, personal_access_token)
    response = requests.get(url, auth=data)
    json_response = response.json()
    print(json_response.get("id"))
    pass


if __name__ == "__main__":
    main()

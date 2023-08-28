#!/usr/bin/python3
'''
    python3 -c 'print(__import__("requests").__doc__)'
'''
import requests
import sys


def main():
    '''
        python3 -c 'print(__import__("requests").main().__doc__)'
        main function
    '''
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(response.text)
    else:
        print("Error: {}".format(response.status_code))


if __name__ == "__main__":
    main()

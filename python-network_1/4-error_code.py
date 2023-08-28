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
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    body = response.text

    if request.status_code >= 400:
        print("Error: {}".format(request.get.status_code))
    else:
        print(body)


if __name__ == "__main__":
    main()

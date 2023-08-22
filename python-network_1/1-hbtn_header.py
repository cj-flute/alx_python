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
    r = sys.argv[1]
    the_url = requests.get(r)
    if 'X-Request-ID' in the_url.headers:
        x_request_id = the_url.headers['X-Request-ID']
        print(x_request_id)


if __name__ == "__main__":
    main()

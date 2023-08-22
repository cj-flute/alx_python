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

    r = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    the_url = requests.post(r, data=payload)

    if r.status_code == 200:
        print(r.text)
    else:
        print("Error: Status code {}".format(r.status_code))


if __name__ == "__main__":
    main()

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
        print("Usage: python script.py <URL> <letter>")
        sys.exit(1)

    url = sys.argv[1]
    q = sys.argv[2]
    if sys.argv[2] == None:
        q = ""
    payload = {'letter': q}
    response = requests.post(url, data=payload)

    if type(response.text) == dict:
        print(response.text)
    elif response.text == {}:
        print("No result")
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()

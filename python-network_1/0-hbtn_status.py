#!/usr/bin/python3
'''
    python3 -c 'print(__import__("requests").__doc__)'
'''
import requests


def main():
    '''
        python3 -c 'print(__import__("requests").my_function.__doc__)'
        main function
    '''
    r = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("         - type: {}".format(type(str(r._content))))
    print("         - content: {}".format(r.content.decode()))


if __name__ == "__main__":
    main()

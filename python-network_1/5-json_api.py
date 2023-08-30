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

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    response = requests.post(url, data=payload)

    try:
        json_res = response.json()
        if not json_res:
            print("No result")
        else:
            id = json_res.get("id")
            name = json_res.get("name")
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()

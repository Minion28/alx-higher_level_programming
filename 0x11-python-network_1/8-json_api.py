#!/usr/bin/python3
'''
script that takes in a letter ans sends a POST request to http://0.0.0.5000/search_user with letter as parameter
'''

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    payload = {'q': arg}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        response.raise_for_status()
        json = response.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")

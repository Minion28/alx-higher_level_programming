#!/usr/bin/python3
'''
script that takes in a url, sends a request to the url and displays body of the response
'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        response.raise_for_status()
        print(response.text)
    except Exception as exc:
        print("Error code: {}".format(response.status_code))

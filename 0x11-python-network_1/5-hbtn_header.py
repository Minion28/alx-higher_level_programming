#!/usr/bin/python3
'''
takes in a url and displays the variable X-request-Id in response header
'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

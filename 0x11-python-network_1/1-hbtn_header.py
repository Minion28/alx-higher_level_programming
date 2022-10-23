#!/usr/bin/python3
'''
script that takes url, and displays value of the X-request-Id variable found in header response
'''

import urllib.request as request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-request-Id'])
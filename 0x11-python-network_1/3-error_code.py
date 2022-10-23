#!/usr/bin/python3
'''
Take in a URL, send a request to URL, and displays the body of response decoded in utf-8
'''

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as err:
        print("Error code: {}".format(err.code))

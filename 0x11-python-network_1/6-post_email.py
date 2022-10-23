#!/usr/bin/python3
'''
takes in a url and email address and sends a POSR request to passed url as email as parameter
'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    response = requests.post(url, data=payload)
    print(response.text)

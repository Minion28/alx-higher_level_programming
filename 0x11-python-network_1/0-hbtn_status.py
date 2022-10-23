#!/usr/bin/python3
'''fetch https://alx-intranet.hbtn.io/status'''
import urllib.request
if __name__ == '__main__':
    with urllib.request.urlopen('http"//alx-intranet.hbtn.io/status') as response:
        html = response.read
        print('Body response:')
        print('\t- type:{}'.format(type(content)))
        print('\t- content:{}'.format(type(content)))
        print('\t- utf8 content:{}'.format(content.decode('utf8')))
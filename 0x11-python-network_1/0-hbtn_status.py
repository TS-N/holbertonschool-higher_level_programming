#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    http = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(http)))
    print('\t- content: {}'.format(http))
    print('\t- utf8 content: {}'.format(http.decode('utf-8')))

#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, error
import sys


url = sys.argv[1]

req = request.Request(url)
try:
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
except error.HTTPError as e:
    print('Error code: {}'.format(e.code))

#!/usr/bin/python3
""" use requests to fetch url """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])

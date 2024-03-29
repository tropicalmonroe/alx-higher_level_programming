#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response."""

if __name__ == "__main__":
    import urllib.request
    import sys

    web = sys.argv[1]
    with urllib.request.urlopen(web) as respo:
        print(respo.headers.get('X-Request-Id'))

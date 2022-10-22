#!/usr/bin/python3
""" script that takes in a URL,sends a request to the URL and display value """
if __name__ == '__main__':
    import sys
    import urllib.request

    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        print(response.header.get('X-Request-Id'))

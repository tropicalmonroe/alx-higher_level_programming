#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    web = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    ask = urllib.request.Request(web, data)
    with urllib.request.urlopen(ask) as respo:
        print(respo.read().decode('utf-8'))


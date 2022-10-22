#!/usr/bin/python3
"""  a Python script that takes in a URL, sends a request to the URL """

if __name__ == "__main__":
    import requests
    from sys import argv

    web = argv[1]
    val = 'X-Request-Id'
    html = requests.get(web)
    print(html.headers.get(val))

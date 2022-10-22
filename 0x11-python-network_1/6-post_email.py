#!/usr/bin/python3
""" This script takes in a URL and an email address, sends a POST """

if __name__ == "__main__":
    import requests
    from sys import argv

    web = argv[1]
    email = argv[2]
    val = {'email': email}
    request = requests.post(web, data=val)
    print(request.text)

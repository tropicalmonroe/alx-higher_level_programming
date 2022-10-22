#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    request = requests.get(url, auth=(username, password))
    print(request.json().get('id'))

#!/usr/bin/python3
""" takes in a URL, sends a request to the URL n display the body response """

if __name__ == "__main__":
    import requests
    from sys import argv

    web = argv[1]
    req = requests.get(web)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)

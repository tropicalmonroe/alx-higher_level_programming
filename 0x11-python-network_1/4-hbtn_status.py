#!/usr/bin/python3
""" a Python script that fetches """

if __name__ == "__main__":
    import requests

    web = 'https://alx-intranet.hbtn.io/status'
    hypertext = requests.get(web)
    print("Body response:")
    print("\t- type: {}".format(type(hypertext.text)))
    print("\t- content: {}".format(hypertext.text))

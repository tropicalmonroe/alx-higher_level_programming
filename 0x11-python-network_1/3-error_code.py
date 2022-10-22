#!/usr/bin/python3
""" takes in a URL sends a req to the URL and displays the bodys response """

if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import HTTPError

    try:
        web = sys.argv[1]
        with urllib.request.urlopen(web) as respo:
            print(respo.read().decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))

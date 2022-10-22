#!/usr/bin/python3
""" sends a POST request to url with the letter as a parameter """

if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    val = argv[1] if len(argv) > 1 else ""
    request = requests.post(url, data={'q': val})
    try:
        _dict = request.json()
        if _dict == {}:
            print('No result')
        else:
            print("[{}] {}".format(_dict.get('id'), _dict.get('name')))
    except ValueError:
        print('Not a valid JSON')

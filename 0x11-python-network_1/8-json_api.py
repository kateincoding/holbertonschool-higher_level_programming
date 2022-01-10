#!/usr/bin/python3
"""Script that takes your GitHub credentials"""


if __name__ == "__main__":
    import sys
    import requests
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    try:
        response = requests.post(url, data)
        json = response.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    except:
        print("Not a valid JSON")

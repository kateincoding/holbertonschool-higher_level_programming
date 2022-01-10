#!/usr/bin/python3
"""github credentials"""


if __name__ == "__main__":
    from requests import get, auth
    import sys
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    response = get(url, auth=auth.HTTPBasicAuth(user, passw))
    try:
        js = response.json()
        print(js.get('id'))
    except ValueError:
        print("None")

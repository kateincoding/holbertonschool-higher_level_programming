#!/usr/bin/python3
"""github credentials"""


if __name__ == "__main__":
    from requests import get, auth
    import sys
    user = sys.argv[1]
    passw = sys.argv[2]
    url = 'https://api.github.com/user'
    r = get(url, auth=auth.HTTPBasicAuth(user, passw))
    try:
        js = r.json()
        print(js.get('id'))
    except ValueError:
        print("Not a valid JSON")

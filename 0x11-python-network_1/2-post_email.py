#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        answer = response.read().decode('utf-8')
        print(answer)

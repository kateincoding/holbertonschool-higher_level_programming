#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        print("    - utf8 content: {}".format(data.decode("utf-8")))

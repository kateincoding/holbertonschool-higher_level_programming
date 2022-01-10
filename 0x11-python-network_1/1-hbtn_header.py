#!/usr/bin/python3
"""script that shows the header value"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        answer = resp.info().get('X-Request-Id')
        print(answer)

#!/usr/bin/python3
"""Error Code"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as data:
            html = data.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

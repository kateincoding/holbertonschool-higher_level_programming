#!/usr/bin/python3
"""Script that displays X-Request-Id in the response header"""


if __name__ == "__main__":
    import requests
    import sys
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))

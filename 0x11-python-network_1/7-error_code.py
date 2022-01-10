#!/usr/bin/python3
"""Error code with requests"""


if __name__ == "__main__":
    import sys
    import requests
    response = requests.get(sys.argv[1])
    status_code = response.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(response.text)

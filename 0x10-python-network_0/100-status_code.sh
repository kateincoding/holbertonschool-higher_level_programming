#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl --write-out %{http_code} --silent --output /dev/null "$1"

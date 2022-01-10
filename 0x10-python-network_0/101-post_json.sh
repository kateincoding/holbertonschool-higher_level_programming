#!/bin/bash
#  request to a URL passed as the first argument, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

#!/bin/bash
# Bash script that sends a DELETE request to the URL passed
# as the first argument and displays the body of the response

curl -sI -X OPTIONS 0.0.0.0:5000/route_4 | grep "Allow" | cut -d ' ' -f2-   

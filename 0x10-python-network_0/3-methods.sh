#!/bin/bash
# Bash script that sends a DELETE request to the URL passed
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-   

#!/bin/bash
#catch content-lenght
curl -sI "$1" | grep -i Content-Length: | cut -d ' ' -f2

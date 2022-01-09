#!/usr/bin/python3
#catch content-lenght

curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2

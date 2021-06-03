#!/usr/bin/python3
"""Module to write a script of dict of Filesize and code_status"""
import sys


filesize = 0
count = 0
stc = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        line = line.split()

        try:
            filesize += int(line[-1])
        except Exception:
            pass

        try:
            code = line[-2]
            if code in list(stc.keys()):
                stc[code] += 1
        except Exception:
            pass
        count += 1

        if count % 10 == 0:
            print("File size: {:d}".format(filesize))
            for key in sorted(stc.keys()):
                if stc[key] != 0:
                    print("{:s}: {:d}".format(key, stc[key]))

    print("File size: {:d}".format(filesize))
    for key in sorted(stc.keys()):
        if stc[key] != 0:
            print("{}: {:d}".format(key, stc[key]))

except KeyboardInterrupt:
    print("File size: {:d}".format(filesize))
    for key in sorted(stc.keys()):
        if stc[key] != 0:
            print("{:s}: {:d}".format(key, stc[key]))
    raise

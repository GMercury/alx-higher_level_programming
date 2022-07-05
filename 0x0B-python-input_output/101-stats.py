#!/usr/bin/python3
"""
Take stdin and check the input, make some operation on it
"""
import sys

errorCode = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
numOfLine = 0
sumSize = 0

try:
    for line in sys.stdin:
        lineToken = line.split()
        if len(lineToken) >= 2:
            tmp = numOfLine
            if lineToken[-2] in errorCode:
                errorCode[lineToken[-2]] += 1
            numOfLine += 1
            sumSize += int(lineToken[-1])
        if numOfLine % 10 == 0:
            print("File size: {:d}".format(sumSize))
            for key, value in sorted(errorCode.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(sumSize))
    for key, value in sorted(errorCode.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(sumSize))
    for key, value in sorted(errorCode.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

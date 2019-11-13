#!/usr/bin/env python3
import sys

def printInvalidUsageErrorMessage():
    sys.stderr.write("Invalid usage! Invalid number of arguments.\n")
    sys.stderr.write("Correct usage: encode.py [task] [filename]\n")
    sys.stderr.write("For help, use: encode.py -h")
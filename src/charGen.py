#!/usr/bin/env python3
"""
Helper script for generating characters
usage: charGen.py [char] [howMany]
"""
import sys

def generateChar(char, number):
    with open(char + '_gen.txt', 'w') as f:
        for elem in range(0, number):
            f.write(char)

args = sys.argv
generateChar(args[1], int(args[2]))
#!/usr/bin/env python3
import sys

def printInvalidUsageErrorMessage():
    sys.stderr.write("Invalid usage! Invalid number of arguments.\n")
    sys.stderr.write("Correct usage: encode.py [task] [filename]\n")
    sys.stderr.write("For help, use: encode.py -h")

def display(statOrCodes):
    if len(statOrCodes[0]) == 3:
        displayStatistic(statOrCodes)
    elif len(statOrCodes[0]) == 4:
        displayShannonFanoCodes(statOrCodes)

"""Displays the values stored in a list of lists containing character statistics information.
Writes the values to stats.txt as well as to stdout

:param stat: list of lists containing symbols, their number of appearances and the percentage
"""    
def displayStatistic(stat):
    with open('stats.txt', 'w') as f:
        for elem in stat:
            line = f"'{elem[0]}': {elem[1]} {elem[2]:.2f}%"
            outputLine(f, line)

"""Displays the values stored in a list of lists containing character statistics information and the Shannon-Fano code.
Writes the values to codes.txt as well as to stdout

:param stat: list of lists containing symbols, their number of appearances,
 the percentage and their Shannon-Fano code
"""    
def displayShannonFanoCodes(codes):
    with open('codes.txt', 'w') as f:
        for elem in codes:
            line = f"'{elem[0]}': {elem[1]} {elem[2]:.2f}% '{elem[3]}'"
            outputLine(f, line)

def displayOptimality(optimality):
    with open('codes.txt', 'a') as f:
        line = "-------------------------------------"
        outputLine(f, line)
        line = f"Average code length: {optimality[0]:.3f}"
        outputLine(f, line)
        line = f"Minimum code length: {optimality[1]:.3f}"
        outputLine(f, line)
        line = f"Optimality: {optimality[2]:.3f}"
        outputLine(f, line)
        line = f"Compression ratio: {optimality[3]:.3f}"
        outputLine(f, line)


def outputLine(f, line):
    print(line)
    f.write(line + "\n")
        
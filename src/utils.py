#!/usr/bin/env python3
import sys
from EncodeNode import EncodeNode

def printInvalidUsageErrorMessage():
    sys.stderr.write("Invalid usage! Invalid number of arguments.\n")
    sys.stderr.write("Correct usage: encode.py [task] [filename]\n")
    sys.stderr.write("For help, use: encode.py -h")

def display(encodeNodes):
    if encodeNodes[0].code == '':
        displayStatistic(encodeNodes)
    else:
        displayCodes(encodeNodes)

"""Displays the values stored in a list of lists containing character statistics information.
Writes the values to stats.txt as well as to stdout

:param stat: list of lists containing symbols, their number of appearances and the percentage
"""    
def displayStatistic(encodeNodes):
    with open('stats.txt', 'w') as f:
        for node in encodeNodes:
            line = f"'{node.symbol}': {node.count} {node.prob:.2f}%"
            outputLine(f, line)

"""Displays the values stored in a list of lists containing character statistics information and the Shannon-Fano code.
Writes the values to codes.txt as well as to stdout

:param stat: list of lists containing symbols, their number of appearances,
 the percentage and their Shannon-Fano code
"""    
def displayCodes(encodeNodes):
    with open('codes.txt', 'w') as f:
        for node in encodeNodes:
            line = f"'{node.symbol}': {node.count} {node.prob:.2f}% '{node.code}'"
            outputLine(f, line)

def displayArithmeticCode(code, blockSize = 20):
    codeArray = [(code[i : i + blockSize]) for i in range(0, len(code), blockSize)] 
    for c in codeArray:
        print(c)

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
        
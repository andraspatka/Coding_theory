#!/usr/bin/env python3
import operator
import collections

"""Creates a statistic of the symbols found in the input file
:param fileName: path to the input file

:returns: 
    A dictionary containing the symbols and their number of occurences in the input file.
    The dictionary is sorted based on the character occurences in descending order.
"""
def createStatistic(filePath):
    stat = {}

    with open(filePath, "r") as f:
        f = open(filePath, "r")
        line = f.readline()
        while line:
            line = list(filter(lambda x: x != '\n', list(line)))
            for c in line:
                if c not in stat:
                    stat[c] = 1
                else:
                    stat[c] = stat[c] + 1
            line = f.readline()
    return sorted(stat.items(), key=operator.itemgetter(1), reverse=True)

"""Displays the values stored in a dictionary
:param stat: dictionary containing symbols and their number of appearances
"""    
def displayStatistic(stat):
    charNum = 0
    for elem in stat:
        charNum += elem[1]
    print("Total number of characters: " + str(charNum))
    with open('out.txt', 'w') as f:
        for elem in stat:
            p = elem[1] / charNum * 100
            line = f"'{elem[0]}': {elem[1]} {p:.2f}%"
            print(line)
            f.write(line + "\n")

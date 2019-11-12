#!/usr/bin/env python3
import operator
import collections

"""Creates a statistic of the symbols found in the input file
:param fileName: path to the input file

:returns: 
    A dictionary containing the symbols, their number of occurences and the percentage in the input file.
    The dictionary is sorted based on the character occurences in descending order.
"""
def createStatistic(filePath):
    stat = {}
    charNum = 0
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
                charNum += 1
            line = f.readline()
    stat = sorted(stat.items(), key=operator.itemgetter(1), reverse=True)
    return [tup + (tup[1]/charNum * 100,) for tup in stat]

"""Displays the values stored in a dictionary
:param stat: dictionary containing symbols, their number of appearances and the percentage
"""    
def displayStatistic(stat):
    with open('out.txt', 'w') as f:
        for elem in stat:
            line = f"'{elem[0]}': {elem[1]} {elem[2]:.2f}%"
            print(line)
            f.write(line + "\n")

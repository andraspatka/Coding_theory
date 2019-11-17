#!/usr/bin/env python3
import operator
import collections

"""Creates a statistic of the symbols found in the input file
:param fileName: path to the input file

:returns: 
    A dictionary containing the symbols, their number of occurrences and the percentage in the input file.
    The dictionary is sorted based on the character occurrences in descending order.
"""
def createStatistic(filePath):
    stat = {}
    charNum = 0
    with open(filePath, "r", encoding='utf-8-sig') as f:
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



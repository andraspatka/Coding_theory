#!/usr/bin/env python3
import operator
import collections
import math
from EncodeNode import EncodeNode

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
    return [EncodeNode(symbol = s[0], count = s[1], prob = (s[1]/charNum * 100)) for s in stat]

"""Returns the metrics determining the encoding's optimality
:param codes: the list of 4 length lists where:
    0 - character code
    1 - character's number of appearances
    2 - probability
    3 - character's Shannon-Fano code

:return:
    a three element array, where:
        0 - average code length
        1 - minimum code length
        2 - optimality
        3 - compression ratio
"""
def getOptimality(encodeNodes):
    for e in encodeNodes:
        e.prob = e.prob / 100
    avg = sum([e.prob * len(e.code) for e in encodeNodes])
    min = - sum([e.prob * math.log(e.prob, 2) for e in encodeNodes])
    opt = min / avg
    compRatio = math.ceil(math.log2(len(encodeNodes))) / avg

    return [avg, min, opt, compRatio]

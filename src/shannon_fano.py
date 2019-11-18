#!/usr/bin/env python3
import stats
import statistics
import math

"""Defines the Shannon-Fano code of the given characters.
:param fileName: path to the input file

:returns: A list of lists, where:
            0 - character code
            1 - character's number of appearances
            2 - probability
            3 - character's Shannon-Fano code
"""
def shannonFano(fileName):
    stat = stats.createStatistic(fileName)
    codes = [list(tup + ('',)) for tup in stat]
    
    encode(codes)
    return codes

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
"""
def getOptimality(codes):
    avg = avgCodeLength(codes)
    min = minCodeLength(codes)
    opt = min / avg

    return [avg, min, opt]

"""Returns the avarage code length
:param codes: the list of 4 length lists where:
    0 - character code
    1 - character's number of appearances
    2 - probability
    3 - character's Shannon-Fano code

:return:
    the avarage code length
"""
def avgCodeLength(codes):
    return sum([c[2] / 100 * len(c[3]) for c in codes])

"""Returns the minimum code length
:param codes: the list of 4 length lists where:
    0 - character code
    1 - character's number of appearances
    2 - probability
    3 - character's Shannon-Fano code

:return:
    the minimum code length
"""
def minCodeLength(codes):
    codes = [[c[0], c[1], c[2] / 100, c[3]] for c in codes ]
    return - sum([c[2] * math.log(c[2], 2) for c in codes])

"""Convenience method for calling encodeRecursive(codes, start, end, code)
:param codes: the list of 4 length lists containing character information
"""
def encode(codes):
    encodeRecursive(codes, 0, len(codes))

"""Recursive implementation of the Shannon-Fano coding algorithm.

:param codes: the list of 4 length lists where:
    0 - character code
    1 - character's number of appearances
    2 - probability
    3 - character's Shannon-Fano code
:param start: the starting index (inclusive)
:param end: the ending index (exclusive)
"""
def encodeRecursive(codes, start, end):
    if end - start <= 1:
        return
    part = indexToPartAt(codes, start, end)

    encodeRecursive(codes, start, part)
    addCode(codes, start, part, '0')
    encodeRecursive(codes, part, end)
    addCode(codes, part, end, '1')

"""Adds the given code ('0' or '1') to the character's Shannon-Fano code.
:param codes: the list of 4 length lists containing character information
:param start: the starting index (inclusive)
:param end: the ending index (exclusive)
:param code: the code to add:
"""
def addCode(codes, start, end, code):
    for i in range(start, end):
        codes[i][3] = code + codes[i][3]


"""Returns the index where parting the given array is advantageous.
:param codes: the list of 4 length lists containing character information
:param start: the starting index (inclusive)
:param end: the ending index (exclusive)

:returns:
    the index where parting the given array is advantageous.
"""
def indexToPartAt(codes, start, end):    
    if end - start <= 1:
        return start
    sum = desired = backSum = 0
    for i in range(start, end):
        desired += codes[i][2]
    desired /= 2
    for i in range(start, end):
        sum += codes[i][2]
        if sum == desired:
            return i + 1
        elif sum > desired:
            j = end - 1
            while backSum < desired:
                backSum += codes[j][2]
                j -= 1
            return i + 1 if abs(desired - sum) < abs(desired - backSum) else j + 1
    return

#!/usr/bin/env python3
import stats
from EncodeNode import EncodeNode

"""Defines the Shannon-Fano code of the given characters.
:param fileName: path to the input file

:returns: A list of lists, where:
            0 - character code
            1 - character's number of appearances
            2 - probability
            3 - character's Shannon-Fano code
"""
def encode(fileName):
    encodeNodes = stats.createStatistic(fileName)
    
    shannonFanoRecursive(encodeNodes, 0, len(encodeNodes))
    return encodeNodes

"""Recursive implementation of the Shannon-Fano coding algorithm.

:param codes: the list of 4 length lists where:
    0 - character code
    1 - character's number of appearances
    2 - probability
    3 - character's Shannon-Fano code
:param start: the starting index (inclusive)
:param end: the ending index (exclusive)
"""
def shannonFanoRecursive(encodeNodes, start, end):
    if end - start <= 1:
        return
    part = indexToPartAt(encodeNodes, start, end)

    addCode(encodeNodes, start, part, '0')
    shannonFanoRecursive(encodeNodes, part, end)
    addCode(encodeNodes, part, end, '1')

"""Adds the given code ('0' or '1') to the character's Shannon-Fano code.
:param codes: the list of 4 length lists containing character information
:param start: the starting index (inclusive)
:param end: the ending index (exclusive)
:param code: the code to add:
"""
def addCode(encodeNodes, start, end, code):
    for i in range(start, end):
        encodeNodes[i].code = code + encodeNodes[i].code


"""Returns the index where parting the given array is advantageous.
:param codes: the list of 4 length lists containing character information
:param start: the starting index (inclusive)
:param end: the ending index (exclusive)

:returns:
    the index where parting the given array is advantageous.
"""
def indexToPartAt(encodeNodes, start, end):    
    if end - start <= 1:
        return start
    sum = desired = backSum = 0
    for i in range(start, end):
        desired += encodeNodes[i].prob
    desired /= 2
    for i in range(start, end):
        sum += encodeNodes[i].prob
        if sum == desired:
            return i + 1
        elif sum > desired:
            j = end - 1
            while backSum < desired:
                backSum += encodeNodes[j].prob
                j -= 1
            return i + 1 if abs(desired - sum) < abs(desired - backSum) else j + 1
    return

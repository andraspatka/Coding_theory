#!/usr/bin/env python3
import math
import stats
import file_reader as fr

from EncodeNode import EncodeNode

"""
Performs an arithmetic coding on the input file
"""
def encode(filePath, blockSize):
    encodeNodes = stats.createStatistic(filePath, sortIt = False)
    encodeNodes = [EncodeNode(symbol = e.symbol, prob = e.prob / 100) for e in encodeNodes]

    encodeNodesCopy = [None] * len(encodeNodes)
    
    encodeNodes[0].interval = (0, encodeNodes[0].prob)
    encodeNodesCopy[0] = EncodeNode(symbol = encodeNodes[0].symbol, prob = encodeNodes[0].prob, interval = encodeNodes[0].interval)
    for i in range(1, len(encodeNodes)):
        lowerBound = encodeNodes[i-1].interval[1]
        encodeNodes[i].interval = (lowerBound, lowerBound + encodeNodes[i].prob)

        encodeNodesCopy[i] = EncodeNode(symbol = encodeNodes[i].symbol, prob = encodeNodes[i].prob, interval = encodeNodes[i].interval)

    fp = fr.openFile(filePath)
    arithmeticCode = ""
    while True:
        block = fr.getNextBlock(fp, blockSize)
        if block == False:
            break
        arithmeticCode = arithmeticCode + encodeArithmetic(block, encodeNodes)
        # Reset the encodeNodes array
        i = 0
        for e in encodeNodesCopy:
            encodeNodes[i] = EncodeNode(symbol = e.symbol, prob = e.prob, interval = e.interval)
            i += 1
        
    fr.closeFile(fp)
    return arithmeticCode

"""
Returns the arithmetic code of the given block
"""
def encodeArithmetic(block, encodeNodes):
    probProd = 1
    for b in block:
        # Search for the actual symbol in the encodeNodes array
        actualNode = EncodeNode()
        for e in encodeNodes:
            if e.symbol == b:
                actualNode = e
                probProd *= actualNode.prob # The product of all the symbols' probabilities
                break
        # Save the symbol's lower and upper bound value
        actualLowerBound = actualNode.interval[0]
        actualUpperBound = actualNode.interval[1]
        intervalLen = actualUpperBound - actualLowerBound
        # Split the interval
        encodeNodes[0].interval = (actualLowerBound, actualLowerBound + intervalLen * encodeNodes[0].prob)
        for i in range(1, len(encodeNodes)):
            lowerBound = encodeNodes[i-1].interval[1]
            # lower bound is equal to the previous value's upper bound
            # upper bound is equal to: lower bound + length of the interval * the symbol's probability
            encodeNodes[i].interval = (lowerBound, lowerBound + intervalLen * encodeNodes[i].prob)
    print(block)

    codeLen = int(math.log(1 / probProd, 2)) + 1 # calculate the desired code length
    tag = (actualLowerBound + actualUpperBound) / 2 # calculate the tag
    code = convertToCode(tag, codeLen)
    print(code)
    
    return code

"""
Converts a floating point number to binary
"""
def convertToCode(realNum, codeLen = 10):
    code = ""
    i = 0
    while realNum > 0 and i < codeLen:
        realNum = realNum * 2
        dec, integral = math.modf(realNum) # integral part
        realNum = dec
        code = code + str(int(integral))
        i += 1
    
    return code
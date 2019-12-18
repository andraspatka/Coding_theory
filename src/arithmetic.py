#!/usr/bin/env python3
import math
import stats
import file_reader as fr

from EncodeNode import EncodeNode

def encode(filePath, blockSize):
    encodeNodes = stats.createStatistic(filePath, sortIt = False)
    probMap = {}
    encodeNodes = [EncodeNode(symbol = e.symbol, prob = e.prob / 100) for e in encodeNodes]

    encodeNodes[0].interval = (0, encodeNodes[0].prob)
    for i in range(1, len(encodeNodes)):
        lowerBound = encodeNodes[i-1].interval[1]
        encodeNodes[i].interval = (lowerBound, lowerBound + encodeNodes[i].prob)

    encodeNodesCopy = [None] * len(encodeNodes)
    i = 0
    for e in encodeNodes:
        encodeNodesCopy[i] = EncodeNode(symbol = e.symbol, prob = e.prob, interval = e.interval)
        i += 1

    fp = fr.openFile(filePath)
    arithmeticCode = ""
    while True:
        block = fr.getNextBlock(fp, blockSize)
        if block == False:
            break
        
        #print(encodeNodesCopy)
        arithmeticCode = arithmeticCode + encodeArithmetic(block, encodeNodes)
        #print(encodeNodes)

        i = 0
        for e in encodeNodesCopy:
            encodeNodes[i] = EncodeNode(symbol = e.symbol, prob = e.prob, interval = e.interval)
            i += 1
        
    print(arithmeticCode)
    fr.closeFile(fp)

def encodeArithmetic(block, encodeNodes):
    probProd = 1
    for b in block:
        actualNode = EncodeNode()
        for e in encodeNodes:
            if e.symbol == b:
                actualNode = e
                probProd *= actualNode.prob
                break
        print(actualNode)
        actualLowerBound = actualNode.interval[0]
        actualUpperBound = actualNode.interval[1]
        intervalLen = actualUpperBound - actualLowerBound
        encodeNodes[0].interval = (actualLowerBound, actualLowerBound + intervalLen * encodeNodes[0].prob)
        for i in range(1, len(encodeNodes)):
            lowerBound = encodeNodes[i-1].interval[1]
            encodeNodes[i].interval = (lowerBound, lowerBound + intervalLen * encodeNodes[i].prob)
    print(block)
    codeLen = int(math.log(1 / probProd, 2)) + 1
    print(codeLen)
    print(f"{actualLowerBound}, {actualUpperBound}")
    tag = (actualLowerBound + actualUpperBound) / 2
    print(tag)
    code = convertToCode(tag, codeLen)
    print(code)
    
    return code

def convertToCode(realNum, codeLen):
    code = ""
    i = 0
    while realNum > 0 and i < codeLen:
        realNum = realNum * 2
        dec, integral = math.modf(realNum) # integral part
        realNum = dec
        code = code + str(int(integral))
        i += 1
    
    return code
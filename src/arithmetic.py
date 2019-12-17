#!/usr/bin/env python3
import math
import stats

from EncodeNode import EncodeNode

def encode(fileName, blockLen):
    encodeNodes = stats.createStatistic(fileName)
    

def convertToCode(realNum):
    code = ""
    codeLen = int(math.log(realNum, 2)) + 1
    i = 0
    while realNum > 0:
        realNum = realNum * 2
        dec, integr = math.modf(realNum) # integral part
        realNum = dec
        code = code + str(int(integr))
    
    return code

print(convertToCode(0.6875))
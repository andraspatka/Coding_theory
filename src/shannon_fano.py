#!/usr/bin/env python3
import stats

def shannonFanno(fileName):
    stat = stats.createStatistic(fileName)
    codes = [list(tup + ('',)) for tup in stat]

    start = 0
    while True:
        part = indexToPartAt(stat, start)
        if start >= part:
            break
        for i in range(start, len(stat)):
            print(str(i) + ' f1')
            code = '0' if i <= part else '1'
            codes[i][3] = codes[i][3] + code
        for i in range(start, part):
            print(i)
            code = '0' if i == start else '1'
            codes[i][3] = codes[i][3] + code
        start = part + 1
        #print(part)

    print(codes)

def indexToPartAt(stat, start):
    topSum = 0
    topIndex = 0
    bottomSum = 0
    bottomIndex = 0
    desired = 0
    for i in range(start, len(stat)):
        desired += stat[i][2]
    desired /= 2
    for i in range(start, len(stat)):
        if topSum < desired:
            topIndex = i
            topSum += stat[topIndex][2]
        if bottomSum < desired:
            bottomIndex = len(stat) - i - 1 
            bottomSum += stat[bottomIndex][2]
    return bottomIndex if ((bottomSum - desired) < (topSum - desired)) else topIndex
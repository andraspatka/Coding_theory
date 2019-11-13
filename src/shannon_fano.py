#!/usr/bin/env python3
import stats

def shannonFanno(fileName):
    stat = stats.createStatistic(fileName)
    codes = [list(tup + ('',)) for tup in stat]

    start = 0
    end = len(codes)
    #print(codes)
    #print(indexToPartAt(codes, start, end))
    #print(codes)
    codes = recursive(codes, 0, end, '')
    print(codes)
    #part = indexToPartAt(codes, start, end)
    #print(addCode(codes, start, part, '0'))
    #print(addCode(codes, part, end, '1'))

    #print(codes)
count = 0

def recursive(codes, start, end, code):
    global count
    if count < 20:
        print(f"called: start: {start} end: {end} code: '{code}'")
        count += 1
    if end - start <= 1:
        codes[start][3] = codes[start][3] + code
        return codes
        #addCode(codes, start, end, code)
        #print(codes)
    else:
        part = indexToPartAt(codes, start, end)
        #print(str(part))
        #print(f"called: start: {start} part: {part} end: {end} code: '{code}'")
        codes = recursive(codes, start, part, '0')
        codes = recursive(codes, part, end, '1')

def addCode(codes, start, end, code):
    for i in range(start, end):
        codes[i][3] = codes[i][3] + code
    return codes

def indexToPartAt(codes, start, end):    
    if end - start <= 1:
        return start
    sum = 0
    index = 0
    desired = 0
    for i in range(start, end):
        desired += codes[i][2]
    desired /= 2
    for i in range(start, end):
        if sum < desired:
            index = i
            prevSum = sum
            sum += codes[index][2]
            if sum > desired:
                if ((sum - desired) < (desired - prevSum)):
                    return index
                else:
                    if end - start > 3:
                        return index - 1
                    else:
                        return index
                #return index if ((sum - desired) < (desired - prevSum)) else index - 1
        else:
            return i
    
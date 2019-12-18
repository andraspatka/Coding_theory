#!/usr/bin/env python3

def openFile(filePath):
    return open(filePath)

def getNextBlock(fp, blockSize):
    block = fp.read(blockSize)
    if len(block) == 0:
        return False
    return block

def closeFile(fp):
    fp.close()
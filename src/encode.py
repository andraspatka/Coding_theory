#!/usr/bin/env python3
"""
Script for displaying probabilities and encoding a source using Shannon-Fano
Usage:  encode.py [task] [filename]
        Available tasks:    -d:  creates and displays the symbol appearance statistics
                            -sf: performs a shannon-fano encoding
                            -h:  displays the help message
"""
import operator
import collections
import sys
import errno
import os
import stats
import shannon_fano
import utils
import huffman
import arithmetic

arguments = sys.argv

TASK_DISPLAY = "-d"
TASK_SF = "-sf"
TASK_HUFF = "-hf"
TASK_SF_STAT = "-sfs"
TASK_HUFF_STAT = "-hfs"
TASK_ARITH = "-ac"

TASKS = [TASK_DISPLAY, TASK_SF, TASK_HUFF, TASK_SF_STAT, TASK_HUFF_STAT, TASK_ARITH]

if len(arguments) == 1:
    utils.printInvalidUsageErrorMessage()
    sys.exit(errno.EINVAL)

if arguments[1] == "-h":
    print("Usage: encode.py [task] [filename]")
    print(f"Available tasks: {TASK_DISPLAY}:   creates and displays the symbol appearance statistics")
    print(f"                 {TASK_SF}:  performs a shannon-fano encoding")
    print(f"                 {TASK_SF_STAT}: performs a shannon-fano encoding and displays its optimality")
    print(f"                 {TASK_HUFF}:  performs a huffman encoding")
    print(f"                 {TASK_HUFF_STAT}: performs a huffman encoding and displays its optimality")
    print(f"                 {TASK_ARITH}: performs an arithmetic encoding")
    print("                 -h:   displays this message")
    sys.exit()

if len(arguments) != 3 and len(arguments) != 4:
    utils.printInvalidUsageErrorMessage()
    sys.exit(errno.E2BIG)

task = arguments[1]
fileName = arguments[2]
if task == TASK_ARITH:
    blockSize = int(arguments[3])

if task not in TASKS:
    sys.stderr.write(f"Invalid usage! The given task: {task} does not exist!\n")
    sys.stderr.write("For help, use: encode.py -h")
    sys.exit(errno.EINVAL)

if not os.path.exists(fileName):
    sys.stderr.write(f"Could not find input file: {fileName}")
    sys.exit(errno.ENOENT)

if task == TASK_DISPLAY:
    utils.display(stats.createStatistic(fileName))
if task == TASK_SF:
    utils.display(shannon_fano.encode(fileName))
if task == TASK_SF_STAT:
    codes = shannon_fano.encode(fileName)
    utils.display(codes)
    utils.displayOptimality(stats.getOptimality(codes))
if task == TASK_HUFF:
    utils.display(huffman.encode(fileName))
if task == TASK_HUFF_STAT:
    codes = huffman.encode(fileName)
    utils.display(huffman.encode(fileName))
    utils.displayOptimality(stats.getOptimality(codes))
if task == TASK_ARITH:
    code = arithmetic.encode(fileName, blockSize)
    utils.displayArithmeticCode(code)


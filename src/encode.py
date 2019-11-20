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

arguments = sys.argv

TASK_DISPLAY = "-d"
TASK_SF = "-sf"
TASK_SF_STAT = "-sfs"

TASKS = [TASK_DISPLAY, TASK_SF, TASK_SF_STAT]

if len(arguments) == 1:
    utils.printInvalidUsageErrorMessage()
    sys.exit(errno.EINVAL)

if arguments[1] == "-h":
    print("Usage: encode.py [task] [filename]")
    print("Available tasks: -d:   creates and displays the symbol appearance statistics")
    print("                 -sf:  performs a shannon-fano encoding")
    print("                 -sfs: performs a shannon-fano encoding and displays its optimality")
    print("                 -h:   displays this message")
    sys.exit()

if len(arguments) != 3:
    utils.printInvalidUsageErrorMessage()
    sys.exit(errno.E2BIG)

task = arguments[1]
fileName = arguments[2]

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
    utils.display(shannon_fano.shannonFano(fileName))
if task == TASK_SF_STAT:
    codes = shannon_fano.shannonFano(fileName)
    utils.display(codes)
    utils.displayOptimality(shannon_fano.getOptimality(codes))


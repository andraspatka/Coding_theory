#!/usr/bin/env python3
import operator
import collections
import sys
import errno
import os
import stats
import shannon_fano
import utils

arguments = sys.argv

if len(arguments) == 1:
    utils.printInvalidUsageErrorMessage()
    sys.exit(errno.EINVAL)

if arguments[1] == "-h":
    print("Usage: encode.py [task] [filename]")
    print("Available tasks: -d:  creates and displays the symbol appearance statistics")
    print("                 -sf: performs a shannon-fano encoding")
    print("                 -h:  displays this message")
    sys.exit()

if len(arguments) != 3:
    utils.printInvalidUsageErrorMessage()
    sys.exit(errno.E2BIG)

task = arguments[1]
fileName = arguments[2]

if task != "-d" and task != "-sf":
    sys.stderr.write(f"Invalid usage! The given task: {task} does not exist!\n")
    sys.stderr.write("For help, use: encode.py -h")
    sys.exit(errno.EINVAL)

if not os.path.exists(fileName):
    sys.stderr.write(f"Could not find input file: {fileName}")
    sys.exit(errno.ENOENT)

if task == "-d":
    stats.displayStatistic(stats.createStatistic(fileName))
if task == "-sf":
    shannon_fano.shannonFanno(fileName)

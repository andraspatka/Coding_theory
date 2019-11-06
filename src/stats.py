import operator
import collections
import sys
import os

def countSymbols(fileName):
    stat = {}

    with open(fileName, "r") as f:
        f = open(fileName, "r")
        line = f.readline()
        while line:
            line = list(filter(lambda x: x != '\n', list(line)))
            for c in line:
                if c not in stat:
                    stat[c] = 1
                else:
                    stat[c] = stat[c] + 1
            line = f.readline()
    return sorted(stat.items(), key=operator.itemgetter(1), reverse=True)
    
def display(stat):
    print(stat)
    uniqueCharNum = 0
    for elem in stat:
        uniqueCharNum += elem[1]
    print("Total number of unique characters: " + str(uniqueCharNum))
    with open('out.txt', 'w') as f:
        for elem in stat:
            p = elem[1] / uniqueCharNum * 100
            line = f"'{elem[0]}': {elem[1]} {p:.2f}%"
            print(line)
            f.write(line + "\n")

if sys.argv[1] == "-h":
    print("Usage: python stats.py [filename]")
    sys.exit()    

if len(sys.argv) != 2:
    print("Invalid usage! The number of arguments should be exactly one.")
    print("Correct usage: python stats.py [filename]")
    sys.exit()

if not os.path.exists(sys.argv[1]):
    print("Could not find input file: " + sys.argv[1])
    sys.exit()
    
display(countSymbols(str(sys.argv[1])))
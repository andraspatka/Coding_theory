import operator
import collections
import sys
import os

def countSymbols(fileName):
    stat = {}
    try:
        f = open(fileName, "r")
        line = f.readline()
        while line:
            line = list(filter(lambda x: x != '\n', list(line)))
            for elem in line:
                if elem not in stat:
                    stat[elem] = 1
                else:
                    stat[elem] = stat[elem] + 1
            line = f.readline()
    finally:
        f.close()
    
    sorted_stat = sorted(stat.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_stat)
    char_num = 0
    for elem in sorted_stat:
        char_num += elem[1]
    print("Total number of unique characters: " + str(char_num))
    f = open('out.txt', 'w')
    for elem in sorted_stat:
        p = elem[1] / char_num * 100
        line = f"'{elem[0]}': {elem[1]} {p:.2f}%"
        print(line)
        f.write(line + "\n")
    f.close

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
    


countSymbols(str(sys.argv[1]))

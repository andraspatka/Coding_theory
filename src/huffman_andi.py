import operator
import math
from itertools import islice
import time

def split(word): 
    return [char for char in word]

def checkKey(dict, key): 
    if key in dict.keys(): 
        return True
    else: 
        return False

def sortedList(dict):
    sorted_list = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list

def averageCodeWord(dict):
    sum = 0
    for i in dict:
        sum = sum + (i[1] * i[3])
    return sum

def minCodeWord(dict):
    sum = 0
    for i in dict:
        sum = sum + -1 *(i[1] * math.log2(i[1]))
    return sum

def efficiency(codeWord, minCodeWord):
    efficiency = minCodeWord / codeWord
    return efficiency

def checkIfKeyExist(dict, key):
    value = 0
    for i in dict:
        if (i[0] == key):
            value = 1
    if value == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    inputFile  = open("../in.txt", "r")
    for x in inputFile:
        splited_text = split(x)
        all_character = len(splited_text)
        my_dict = {}
        for i in splited_text:
            if (checkKey(my_dict, i) == False):
                my_dict[i] = 1
            else:
                my_dict[i] = (my_dict.get(i)+1)

    stat_dict = {}
    for stat in my_dict:
        stat_dict[stat] = my_dict.get(stat)/all_character

    file = open("statistics_huffman.txt", "w")

    for x in my_dict:
        write_to_file = x + " -> " + str(my_dict.get(x)) + " -> "+ str(stat_dict.get(x))
        file.write(write_to_file)
        file.write("\n")

    sorted_statList = sortedList(stat_dict)
    print(sorted_statList)
    R ={}
    number_of_aggregation = len(sorted_statList) - 2

    current_milli_time = int(round(time.time() * 1000))
    R[0] = sorted_statList
    #create the split list, count how many aggregation it have
    for i in range(number_of_aggregation):
        if i == 0:
            temp = {}
            for element in islice(sorted_statList, len(sorted_statList) - 1):
                if (sorted_statList.index(element)<number_of_aggregation):
                    temp[element[0]] = element[1]
                else:
                    new_element = sorted_statList[len(sorted_statList)-2][0] + sorted_statList[len(sorted_statList)-1][0]
                    new_value = sorted_statList[len(sorted_statList)-2][1] + sorted_statList[len(sorted_statList)-1][1]
                    temp[new_element] = new_value
            R[i+1] = sortedList(temp)
        else:
            temp = {}
            for element in islice(R[i], len(R[i])-1):
                if (R[i].index(element)<len(R[i])-2):
                    temp[element[0]] = element[1]
                else:
                    new_element = R[i][len(R[i])-2][0] + R[i][len(R[i])-1][0]
                    new_value = R[i][len(R[i])-2][1] + R[i][len(R[i])-1][1]
                    temp[new_element] = new_value
            R[i+1] = sortedList(temp)

    for counter in range(len(R) -1, -1, -1):
        R[counter] = [list(elem  + ('',) + ('',)) for elem in R[counter]]
        if (counter == len(R) - 1):
            new_dict = {}
            R[counter][0][2] = "0"
            R[counter][1][2] = "1"
            for elem in R[counter]:
                if (len(elem[0]) != 1):
                    for i in range(1,len(elem[0])):
                        if (checkIfKeyExist(R[counter-1], elem[0][:i])):
                            temporary = elem[0]
                            old_value1 = elem[0][:i]
                            old_value2 = elem[0][i:]
                            new_dict[old_value1] = elem[2]
                            new_dict[old_value2] = elem[2]
            for elem in R[counter]:
                if elem[0] != temporary:
                    new_dict[elem[0]] = elem[2]
        else:
            for elem in new_dict:
                for elem_R in R[counter]:
                    if (elem == elem_R[0]):
                        elem_R[2] = new_dict.get(elem)
            new_dict = {}
            # print(R[counter])
            R[counter][len(new_dict)-2][2] = R[counter][len(new_dict)-2][2] + "0"
            R[counter][len(new_dict)-1][2] = R[counter][len(new_dict)-1][2] + "1"
            for elem in R[counter]:
                if (len(elem[0]) != 1):
                    for i in range(1,len(elem[0])):
                        if (checkIfKeyExist(R[counter-1], elem[0][:i])):
                            temporary = elem[0]
                            old_value1 = elem[0][:i]
                            old_value2 = elem[0][i:]
                            new_dict[old_value1] = elem[2]
                            new_dict[old_value2] = elem[2]
            for elem in R[counter]:
                if elem[0] != temporary:
                    new_dict[elem[0]] = elem[2]
    current_milli_time = int(round(time.time() * 1000)) - current_milli_time
    print(f"Futasi ido Andi: {current_milli_time}")

    for elem in new_dict:
        for elem_R in R[0]:
            if (elem == elem_R[0]):
                elem_R[3] = len(new_dict.get(elem))
    
    for elem in new_dict:
        print(str(elem) + " -> " + new_dict.get(elem))

    codeWord = averageCodeWord(R[0])
    print("Average Code Word: " + str(codeWord))
    minCodeWord = minCodeWord(R[0])
    eff = efficiency(codeWord, minCodeWord)
    print("Average code word:  " +  str(codeWord))
    print("Efficiency: " + str(eff))

    naturalLog = int(math.log2(len(R[0])))+1
    compressionRate = naturalLog / codeWord
    print("Compression rate: " + str(compressionRate))
    
            
    
  
    





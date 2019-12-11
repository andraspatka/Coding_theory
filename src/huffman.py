#!/usr/bin/env python3
import stats
from EncodeNode import EncodeNode

"""
General representation of a tree node
"""
class HeapNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None
 
"""Traverses the max heap and adds the appropriate huffman codes to the leaves.
:param root: the root of the max heap
:param code: the code to add to the leaf
"""
def addCode(root, code=''):   
    if root:
        root.value.code = code
        addCode(root.left, code + '1')
        addCode(root.right, code + '0')
    
"""Converts a heap to a list. Filters out values where the character code is empty.
:param root: the root of the max heap
:param codes: the list the heap is converted to
"""
def heapToList(root, codes): 
    if root:
        if root.value.symbol != '':
            codes.insert(0, root.value)
        heapToList(root.left, codes) 
        heapToList(root.right, codes)

"""Defines the Huffman code of the given characters.
:param fileName: path to the input file

:returns: A list of lists, where:
            0 - character code
            1 - character's number of appearances
            2 - probability
            3 - character's Shannon-Fano code
"""
def encode(fileName):
    encodeNodes = stats.createStatistic(fileName)

    if len(encodeNodes) % 2 == 1:
        encodeNodes.insert(len(encodeNodes), EncodeNode(prob = 0))
    
    return huffman(encodeNodes)

"""Implementation of the Huffman encoding algorithm, using a max heap.

:param codes: the list of 4 length lists where:
    0 - character code
    1 - character's number of appearances
    2 - probability
    3 - character's Shannon-Fano code
"""
def huffman(codes):
    heapNodes = [None] * len(codes)
    for i in range(0, len(codes)):
        heapNodes[i] = HeapNode(codes[i])
    
    while len(heapNodes) > 1:
        left = heapNodes[len(heapNodes) - 1]
        right = heapNodes[len(heapNodes) - 2]

        root = HeapNode(EncodeNode(prob = left.value.prob + right.value.prob))
        root.left = left
        root.right = right

        heapNodes = heapNodes[0 : len(heapNodes) - 2]
        heapNodes.insert(0, root)
        heapNodes.sort(key = lambda h : h.value.prob, reverse = True)

    addCode(heapNodes[0]) # heapNodes[0] is the root
    codes = []
    heapToList(heapNodes[0], codes)
    codes.sort(key = lambda c : c.prob, reverse = True)
    return codes

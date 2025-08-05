#!/usr/bin/env python3

import sys
import heapq
import os
import math
import ast

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


def generateCodeTable(node, table, val=''):
    newVal = val + str(node.huff)

    if node.left:
        generateCodeTable(node.left, table, newVal)
    if node.right:
        generateCodeTable(node.right, table, newVal)

    if not node.left and not node.right:
        table[node.symbol] = newVal

# if len(sys.argv) < 2:
#     print("Usage: ./script.py <filename>")
#     sys.exit(1)

# filename = sys.argv[1]

charFreq = {}
nodes = []
codeTable = {}

with open('../../Desktop/compressor/source.txt', 'r') as f:
    for line in f:
        for letter in line:
            charFreq[letter] = charFreq.get(letter, 0) + 1

for key, value in charFreq.items():
    heapq.heappush(nodes, node(value, key))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1
    
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    heapq.heappush(nodes, newNode)

generateCodeTable(nodes[0], codeTable)

printNodes(nodes[0])

# filepath = './output-test.txt'

# if not os.path.exists(filepath):
#     os.mknod(filepath)

# with open(filepath, 'wb') as f:
#     header = str(charFreq) + '\n'
#     f.write(header.encode('utf-8'))

#     bitstream = []
#     size = 0
#     with open(filename, 'r') as input:
#         for line in input:
#             for letter in line:
#                 bitstream.append(codeTable[letter])
#                 size += 1

#     bitstream = ''.join(bitstream)
#     f.write(f'{len(bitstream)}\n'.encode('utf-8'))

#     padding = 8 - len(bitstream) % 8 if len(bitstream) % 8 != 0 else 0
#     bitstream += '0' * padding

#     bytesList = []
#     for i in range(0, len(bitstream), 8):
#         byte = bitstream[i:i+8]
#         byteVal = int(byte, 2)
#         bytesList.append(byteVal)
    
#     f.write(bytes(bytesList))

# header = ''

# with open(filepath, 'rb') as f:
#     header = f.readline().decode('utf-8').strip()
#     freq = ast.literal_eval(header)
#     length = int(f.readline().decode('utf-8').strip())
#     nodes = []
#     table = {}
    
#     for key, value in freq.items():
#         heapq.heappush(nodes, node(value, key))

#     while len(nodes) > 1:
#         left = heapq.heappop(nodes)
#         right = heapq.heappop(nodes)

#         left.huff = 0
#         right.huff = 1

#         newNode = node(left.freq + right.freq, left.symbol+ right.symbol, left, right)
#         heapq.heappush(nodes, newNode)

#     generateCodeTable(nodes[0], table)
    
#     bytesList = []
#     for byte in f.read():
#         bytesList.append(bin(byte)[2:].zfill(8))

#     bitstream = ''.join(bytesList)
#     decodedString = []

#     curr = 0
#     while curr < length:
#         currBit = bitstream[curr]
#         currNode = nodes[0]
#         while currNode.left or currNode.right:
#             if currBit == '1':
#                 currNode = currNode.right
#             elif currBit == '0':
#                 currNode = currNode.left

#             curr += 1
            
#             if curr < length:
#                 currBit = bitstream[curr]
#             else:
#                 break

#         decodedString.append(currNode.symbol)
#     decodedString = ''.join(decodedString)

#     filepath = './decoded.txt'
#     if not os.path.exists(filepath):
#         os.mknod(filepath)

#     with open(filepath, 'w') as f:
#         f.write(decodedString)



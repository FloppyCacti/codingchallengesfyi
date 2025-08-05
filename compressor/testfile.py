#!/usr/bin/env python3

firstFreq = []
secFreq = []

with open('./challenge-huffman/test.txt', 'r') as file:
    for line in file:
        for letter in line:
            firstFreq.append(letter)

with open('./decoded.txt', 'r') as file:
    for line in file:
        for letter in line:
            secFreq.append(letter)
char = 0


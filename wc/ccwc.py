#!/usr/bin/env python3
import argparse
import sys

def totalBytes(fileName, isText):
    if not isText:
        file = open(fileName, 'r').read()
        return len(file.encode('utf-8'))
    else:
        data = fileName;
        return len(data.encode('utf-8'))

def totalLines(fileName, isText):
    res = 0
    if not isText:
        with open(fileName, 'r') as f:
            for line in f:
                res += 1
    else:
        res = len(fileName.split('\n'))
        res -= 1
    return res 

def totalWord(fileName, isText):
    res = 0
    if not isText:
        inWord = False
        with open(fileName, 'r') as f:
            for line in f:
                for letter in line:
                    if letter not in {'\n', '\t', ' ', '\r', '\v', '\f'}:
                        if not inWord:
                            res += 1
                            inWord = True
                    else:
                        inWord = False
    else:
        inWord = False
        for letter in fileName:
            if letter not in {'\n', '\t', ' ', '\r', '\v', '\f'}:
                if not inWord:
                    res += 1
                    inWord = True
            else:
                inWord = False
    return res

def totalChar(fileName, isText):
    res = 0
    if not isText:
        with open(fileName, 'r') as f:
            for line in f:
                for word in line:
                    res += 1
    else:
        for line in fileName:
            for word in line:
                res += 1
    return res

def generateOutput(arg, file, isStd=False):
    if not isStd:
        if arg == "-c":
            print(totalBytes(file, isStd), file)
        elif arg == "-l":
            print(totalLines(file, isStd), file)
        elif arg == "-m":
            print(totalChar(file, isStd), file)
        elif arg == "-w":
            print(totalWord(file, isStd), file)
        else:
            print(totalLines(file, isStd), totalWord(file, isStd), totalBytes(file, isStd), file)
    else:
        if arg == "-c":
            print(totalBytes(file, isStd))
        elif arg == "-l":
            print(totalLines(file, isStd))
        elif arg == "-m":
            print(totalChar(file, isStd))
        elif arg == "-w":
            print(totalWord(file, isStd))
        else:
            print(totalLines(file, isStd), totalWord(file, isStd), totalBytes(file, isStd))


parser = argparse.ArgumentParser()

parser.add_argument("-c", "--byte", action="store_true") 
parser.add_argument("-l", "--lines", action="store_true")
parser.add_argument("-m", "--chars", action="store_true")
parser.add_argument('-w', "--words", action="store_true")
parser.add_argument('file', nargs='?')

args = parser.parse_args()

if args.file:
    if args.byte:
        generateOutput('-c', args.file)
    elif args.lines:
        generateOutput('-l', args.file)
    elif args.chars:
        generateOutput('-m', args.file)
    elif args.words:
        generateOutput('-w', args.file)
    else:
        generateOutput('all', args.file)
    exit()

if not sys.stdin.isatty():
    input = sys.stdin.read()

    if args.byte:
        generateOutput('-c', input, True)
    elif args.lines:
        generateOutput('-l', input, True)
    elif args.words:
        generateOutput('-w', input, True)
    elif args.chars:
        generateOutput('-m', input, True)
    else:
        generateOutput('all', input, True)
    exit()

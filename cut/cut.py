#!/bin/env python3

import sys
import os
import csv

# set default variables
delimiter = '\t'
fvalues = []

if len(sys.argv) > 2 and os.path.exists(sys.argv[-1]):
    # set file name
    filename = sys.argv[-1]
    usestdin = False
elif not sys.stdin.isatty():
    usestdin = True
else:
    raise Exception(f"proper syntax: ./cut.py [arg] [file] or [stdin] | ./cut.py [arg]")
    
# check if arguments are provided
if len(sys.argv) == 2:
    raise Exception(f"no argument was provided")

# read arguments provided and set delimiter and fvalues 
for index, arg in enumerate(sys.argv[1:-1 if sys.argv[-1] != '-' else -2]):
    if arg.startswith("-f") and len(arg) > 2:
        idx = 0
        if ',' in arg:
            fvalues = list(map(int, arg[2:].split(',')))
        elif ' ' in arg:
            fvalues = list(map(int, arg[2:].split(' ')))
        elif len(arg[2:]):
            fvalues = [int(arg[2:])]
        else:
            raise Exception(f'not valid -f value: {letter}')
    elif arg.startswith("-d") and len(arg) > 2:
        # change delimiter
        delimiter = arg[2:]
    else:
        raise Exception("expected value after -f")

# Read from file or stdin
if usestdin:
    readvalue = sys.stdin
elif filename:
    readvalue = open(filename, 'r')
else:
    raise Exception("No input file provided and no stdin detected")

# read csv data
reader = csv.reader(readvalue, delimiter=delimiter)

# print out the result
for row in reader:
    print(delimiter.join(row[idx - 1] for idx in fvalues))

# close the file if open
if not usestdin:
    readvalue.close()

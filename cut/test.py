#!/bin/env python3

import sys

print(sys.argv, end='')
if not sys.stdin.isatty():
    print(sys.stdin.readline())

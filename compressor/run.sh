#!/bin/bash

./script.py ./challenge-huffman/test.txt

echo "char:"
wc -m ./challenge-huffman/test.txt
wc -m decoded.txt
echo ""

echo "byte:"
wc -c ./challenge-huffman/test.txt
wc -c decoded.txt
echo ""

echo "lines:"
wc -l ./challenge-huffman/test.txt
wc -l decoded.txt
echo ""

echo "words"
wc -w ./challenge-huffman/test.txt
wc -w decoded.txt
echo ""

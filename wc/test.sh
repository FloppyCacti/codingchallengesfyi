#!/bin/bash

wc -c test.txt
./ccwc.py -c test.txt
cat test.txt | ./ccwc.py -c 

wc -l test.txt
./ccwc.py -l test.txt
cat test.txt | ./ccwc.py -l 

wc -w test.txt
./ccwc.py -w test.txt
cat test.txt | ./ccwc.py -w 

wc -m test.txt
./ccwc.py -m test.txt
cat test.txt | ./ccwc.py -m 

wc test.txt
./ccwc.py test.txt
cat test.txt | ./ccwc.py 

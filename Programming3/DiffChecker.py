# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:48:02 2017

@author: Shuvrajit
"""

import sys

f1 = open(sys.argv[1])
#f1 = open('train.txt.readable')
f2 = open(sys.argv[2])
#f2 = open('train.txt.readable.ALL')

g1 = f1.read()
g2 = f2.read()

g1split = g1.split('\n')
g2split = g2.split('\n')

l = len(g2split)
i = 0

while(i < l):        
    if g1split[i] != g2split[i]:        
        print "myfile:",g1split[i]
        print "tracefile:",g2split[i]
    i += 1        
f1.close()
f2.close()


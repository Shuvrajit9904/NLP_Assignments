# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:59:58 2017

@author: Shuvrajit
"""

import os
import sys

def isABBR(word):
    word = list(str(word))
    flag = 0
    if len(word) <= 4 and ord(word[-1]) == 46:
        for i in word:
            if ord(i) >= 65 and ord(i) <= 90:
                flag = 1
            elif ord(i) >= 97 and ord(i) <= 122:                 
                flag = 1
            elif ord(i) == 46:
                flag = 1
            else:
                flag = 0
                break
    if flag == 0:
        return 'no'                
    else:
        return 'yes'               

def isCAP(word):
    word = list(str(word))
    if ord(word[0]) >= 65 and ord(word[0]) <= 90:
        return 'yes'
    else:
        return 'no'
    
def isLOC(word):
    if word in locationdict:
        return 'yes'
    else:
        return 'no'
    

#arguments = sys.argv
#possibleFtype = arguments[4:]

f1 = open('ner-input-files/train.txt')
#f1 = open(arguments[1])
trainRaw = f1.read()
trainSplitOnLine = trainRaw.strip().split('\n')

f2 = open('ner-input-files/test.txt')
#f2 = open(arguments[2])
testRaw = f2.read()
testSplitOnLine = testRaw.strip().split('\n')


f3 = open('ner-input-files/locs.txt')
#f3 = open(arguments[3])
locRaw = f3.read()
locSplitOnline = locRaw.strip().split('\n')

locationdict = {}
for loc in locSplitOnline:
    locationdict[loc] = 1

trainWords = {}
trainPOS = {}

possibleFtype = ['WORD', 'WORDCON', 'POS', 'POSCON', 'ABBR', 'CAP', 'LOCATION']

trainlength = len(trainSplitOnLine)
testlength = len(testSplitOnLine)
#for i in range(trainlength):
for i in range(50):    
    line = trainSplitOnLine[i].split()
    if i < (trainlength-1):
        nextline = trainSplitOnLine[i+1].split()
    WORDCON = ['','']
    POSCON = ['','']
    if i == 0:        
        if len(line) != 0:                    
            WORD = line[-1]   
            if WORD in trainWords:
                trainWords[WORD] += 1
            else:
                trainWords[WORD] = 1                                
            POS = line[1]
            if POS in trainPOS:
                trainPOS[POS] += 1
            else:
                trainPOS[POS] = 1                                            
            ABBR = isABBR(WORD)                
            CAP = isCAP(WORD)            
            LOC = isLOC(WORD)
            if len(trainSplitOnLine[i+1].split()) > 0:
                WORDCON = ['PHI', nextline[-1]]
                POSCON = ['PHIPOS', nextline[1]]
            else:
                WORDCON = ['PHI', 'OMEGA']
                POSCON = ['PHIPOS', 'OMEGAPOS']            
    else:
        if len(line) != 0:        
            WORD = line[-1]
            if WORD in trainWords:
                trainWords[WORD] += 1
            else:
                trainWords[WORD] = 1                                            
            POS = line[1]
            if POS in trainPOS:
                trainPOS[POS] += 1
            else:
                trainPOS[POS] = 1                                            
            ABBR = isABBR(WORD)                
            CAP = isCAP(WORD)            
            LOC = isLOC(WORD)
            if len(prevline) == 0:
                WORDCON[0] = 'PHI'
                POSCON[0] = 'PHIPOS'
            else:
                WORDCON[0] = prevline[-1]
                POSCON[0] = prevline[1]
            if i < (trainlength - 1):                
                if len(nextline) == 0:
                    WORDCON[1] = 'OMEGA'
                    POSCON[1] = 'OMEGAPOS'
                else:
                    WORDCON[1] = nextline[-1]
                    POSCON[1] = nextline[1]
            else:
                WORDCON[1] = 'OMEGA' 
                POSCON[1] = 'OMEGAPOS'
                               
    prevline = line                

    if len(line) != 0:  
        if 'WORD' in possibleFtype:
            print "WORD: ", WORD
        else:
            print "WORD: n/a"
        if 'WORDCON' in possibleFtype:            
            print "WORDCON: {} {}".format(WORDCON[0],WORDCON[1])
        else:
            print "WORDCON: n/a"
        if 'POS' in possibleFtype:                        
            print "POS: ", POS
        else:
            print "POS: n/a"            
        if 'POSCON' in possibleFtype:                                    
            print "POSCON: {} {}".format(POSCON[0],POSCON[1])
        else:
            print "POSCON: n/a"            
        if 'ABBR' in possibleFtype:                                                
            print "ABBR: ", ABBR
        else:
            print "ABBR: n/a"
        if 'CAP' in possibleFtype:                                                
            print "CAP: ", CAP
        else:
            print "CAP: n/a"
        if 'LOCATION' in possibleFtype:                                                
            print "LOCATION: ", LOC
        else:
            print "LOCATION: n/a"
        print '\n'

'''
#for i in range(testlength):
for i in range(50):    
    line = testSplitOnLine[i].split()
    if i < (testlength-1):
        nextline = testSplitOnLine[i+1].split()
    WORDCON = ['','']
    POSCON = ['','']
    if i == 0:        
        if len(line) != 0:
            WORD = line[-1]                                                  
            if WORD in trainWords:
                WORD = line[-1]                
            else:
                WORD = 'UNK'
            POS = line[1]
            if POS in trainPOS:
                POS = line[1]
            else:
                POS = 'UNKPOS'                
            ABBR = isABBR(WORD)                
            CAP = isCAP(WORD)            
            LOC = isLOC(WORD)
            if len(trainSplitOnLine[i+1].split()) > 0:
                if nextline[-1] in trainWords:
                    WORDCON = ['PHI', nextline[-1]]
                else:
                    WORDCON = ['PHI', 'UNK']
                if nextline[1] in trainPOS:
                    POSCON = ['PHIPOS', nextline[1]]
                else:
                    POSCON = ['PHIPOS', 'UNKPOS']
            else:
                WORDCON = ['PHI', 'OMEGA']
                POSCON = ['PHIPOS', 'OMEGAPOS']            
    else:        
        if len(line) != 0:        
            WORD = line[-1]
            if WORD in trainWords:
                WORD = line[-1]                
            else:
                WORD = 'UNK'
            POS = line[1]
            if POS in trainPOS:
                POS = line[1]
            else:
                POS = 'UNKPOS'                            
            ABBR = isABBR(WORD)                
            CAP = isCAP(WORD)            
            LOC = isLOC(WORD)
            if len(prevline) == 0:
                WORDCON[0] = 'PHI'
                POSCON[0] = 'PHIPOS'
            else:
                if prevline[-1] in trainWords:
                    WORDCON[0] = prevline[-1]
                else:
                    WORDCON[0] = 'UNK'
                if prevline[1] in trainPOS:                    
                    POSCON[0] = prevline[1]
                else:
                    POSCON[0] = 'UNKPOS'                    
            if i < (testlength - 1):                
                print "i:",i
                if len(nextline) == 0:
                    WORDCON[1] = 'OMEGA'
                    POSCON[1] = 'OMEGAPOS'
                else:
                    if nextline[-1] in trainWords:
                        WORDCON[1] = nextline[-1]
                    else:
                        WORDCON[1] = 'UNK'
                    if nextline[1] in trainPOS:
                        POSCON[1] = nextline[1]
                    else:
                        POSCON[1] = 'UNKPOS'
            else:
                WORDCON[1] = 'OMEGA' 
                POSCON[1] = 'OMEGAPOS'
                               
    prevline = line                
    
                
    if len(line) != 0:  
        if 'WORD' in possibleFtype:
            print "WORD: ", WORD
        else:
            print "WORD: n/a"
        if 'WORDCON' in possibleFtype:            
            print "WORDCON: {} {}".format(WORDCON[0],WORDCON[1])
        else:
            print "WORDCON: n/a"
        if 'POS' in possibleFtype:                        
            print "POS: ", POS
        else:
            print "POS: n/a"            
        if 'POSCON' in possibleFtype:                                    
            print "POSCON: {} {}".format(POSCON[0],POSCON[1])
        else:
            print "POSCON: n/a"            
        if 'ABBR' in possibleFtype:                                                
            print "ABBR: ", ABBR
        else:
            print "ABBR: n/a"
        if 'CAP' in possibleFtype:                                                
            print "CAP: ", CAP
        else:
            print "CAP: n/a"
        if 'LOCATION' in possibleFtype:                                                
            print "LOCATION: ", LOC
        else:
            print "LOCATION: n/a"
        print '\n'
'''                
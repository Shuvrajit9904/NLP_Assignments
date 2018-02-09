# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:59:58 2017

@author: Shuvrajit
"""
from __future__ import print_function
#import os
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
    

out1 = 'train.txt.readable'
out11 = open(out1, "w")
out2 = 'test.txt.readable'
out22 = open(out2, "w")
out3 = 'train.txt.vector'
out33 = open(out3, "w")
out4 = 'test.txt.vector'
out44 = open(out4, "w")

arguments = sys.argv
possibleFtype = arguments[4:]

#f1 = open('ner-input-files/train.txt')
f1 = open(arguments[1])
trainRaw = f1.read()
trainSplitOnLine = trainRaw.strip().split('\n')

#f2 = open('ner-input-files/test.txt')
f2 = open(arguments[2])
testRaw = f2.read()
testSplitOnLine = testRaw.strip().split('\n')


#f3 = open('ner-input-files/locs.txt')
f3 = open(arguments[3])
locRaw = f3.read()
locSplitOnline = locRaw.strip().split('\n')

locationdict = {}
for loc in locSplitOnline:
    locationdict[loc] = 1

trainWords = {}
trainPOS = {}

#possibleFtype = ['WORD', 'WORDCON', 'POSCON', 'POS', 'ABBR','CAP', 'LOCATION']

trainlength = len(trainSplitOnLine)
testlength = len(testSplitOnLine)
for i in range(trainlength):
#for i in range(50):    
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
            #print "WORD: ", WORD
            out11.write("WORD: {}".format(WORD))
            out11.write('\n')
        else:
            #print "WORD: n/a"
            out11.write('WORD: n/a')
            out11.write('\n')
        if 'WORDCON' in possibleFtype:            
            #print "WORDCON: {} {}".format(WORDCON[0],WORDCON[1])
            out11.write("WORDCON: {} {}".format(WORDCON[0],WORDCON[1]))
            out11.write('\n')
        else:
            #print "WORDCON: n/a"
            out11.write('WORDCON: n/a')
            out11.write('\n')
        if 'POS' in possibleFtype:                        
            #print "POS: ", POS
            out11.write("POS: {}".format(POS))
            out11.write('\n')
        else:
            #print "POS: n/a"            
            out11.write("POS: n/a")
            out11.write('\n')
        if 'POSCON' in possibleFtype:                                            
            #print "POSCON: {} {}".format(POSCON[0],POSCON[1])
            out11.write("POSCON: {} {}".format(POSCON[0],POSCON[1]))
            out11.write('\n')
        else:
            #print "POSCON: n/a"            
            out11.write("POSCON: n/a")
            out11.write('\n')
        if 'ABBR' in possibleFtype:                                                
            #print "ABBR: ", ABBR
            out11.write("ABBR: {}".format(ABBR))
            out11.write('\n')
        else:
            #print "ABBR: n/a"
            out11.write("ABBR: n/a")
            out11.write('\n')
        if 'CAP' in possibleFtype:                                                
            #print "CAP: ", CAP
            out11.write("CAP: {}".format(CAP))
            out11.write('\n')
        else:
            #print "CAP: n/a"
            out11.write("CAP: n/a")
            out11.write('\n')
        if 'LOCATION' in possibleFtype:                                                
            #print "LOCATION: ", LOC
            out11.write("LOCATION: {}".format(LOC))
            out11.write('\n')
        else:
            #print "LOCATION: n/a"
            out11.write("LOCATION: n/a")
            out11.write('\n')
        #print '\n'
        out11.write('\n')

out11.close()


for i in range(testlength):
#for i in range(50):    
    line = testSplitOnLine[i].split()
    if i < (testlength-1):
        nextline = testSplitOnLine[i+1].split()
    WORDCON = ['','']
    POSCON = ['','']
    if i == 0:        
        if len(line) != 0:
            WORD = line[-1]
            auxWORD = WORD
            if WORD in trainWords:
                WORD = line[-1]                
            else:
                WORD = 'UNK'
            POS = line[1]
            if POS in trainPOS:
                POS = line[1]
            else:
                POS = 'UNKPOS'                
            ABBR = isABBR(auxWORD)        
            CAP = isCAP(auxWORD)                                       
            LOC = isLOC(auxWORD)
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
            auxWORD = WORD
            if WORD in trainWords:
                WORD = line[-1]                
            else:
                WORD = 'UNK'
            POS = line[1]
            if POS in trainPOS:
                POS = line[1]
            else:
                POS = 'UNKPOS'                            
            ABBR = isABBR(auxWORD)             
            CAP = isCAP(auxWORD)                        
            LOC = isLOC(auxWORD)
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
            #print "WORD: ", WORD
            out22.write("WORD: {}".format(WORD))
            out22.write('\n')
        else:
            #print "WORD: n/a"
            out22.write("WORD: n/a")
            out22.write('\n')
        if 'WORDCON' in possibleFtype:            
            #print "WORDCON: {} {}".format(WORDCON[0],WORDCON[1])
            out22.write("WORDCON: {} {}".format(WORDCON[0],WORDCON[1]))
            out22.write('\n')
        else:
            #print "WORDCON: n/a"
            out22.write("WORDCON: n/a")
            out22.write('\n')
        if 'POS' in possibleFtype:                        
            #print "POS: ", POS
            out22.write("POS: {}".format(POS))
            out22.write('\n')
        else:
            #print "POS: n/a"            
            out22.write("POS: n/a")
            out22.write('\n')
        if 'POSCON' in possibleFtype:                                    
            #print "POSCON: {} {}".format(POSCON[0],POSCON[1])
            out22.write("POSCON: {} {}".format(POSCON[0],POSCON[1]))
            out22.write('\n')
        else:
            #print "POSCON: n/a"            
            out22.write("POSCON: n/a")
            out22.write('\n')
        if 'ABBR' in possibleFtype:                                                
            #print "ABBR: ", ABBR
            out22.write("ABBR: {}".format(ABBR))
            out22.write('\n')
        else:
            #print "ABBR: n/a"
            out22.write("ABBR: n/a")
            out22.write('\n')
        if 'CAP' in possibleFtype:                                                
            #print "CAP: ", CAP
            out22.write("CAP: {}".format(CAP))
            out22.write('\n')            
        else:
            #print "CAP: n/a"
            out22.write("CAP: n/a")
            out22.write('\n')
        if 'LOCATION' in possibleFtype:                                                
            #print "LOCATION: ", LOC
            out22.write("LOCATION: {}".format(LOC))
            out22.write('\n')
        else:
            #print "LOCATION: n/a"
            out22.write("LOCATION: n/a")
            out22.write('\n')
        #print '\n'
        out22.write('\n')
out22.close()
#Creating the feature vector in libSVM format

featureTable = {}

k = 1
for key in trainWords:
    word = "-".join(['word',key])    
    featureTable[word] = k
    k += 1
    prevword = "-".join(['prev-word',key])
    featureTable[prevword] = k
    k += 1
    nextword = "-".join(['next-word',key])
    featureTable[nextword] = k
    k += 1
    
#featureTable['word-PHI'] = k
#k += 1
featureTable['prev-word-PHI'] = k
k += 1
featureTable['next-word-OMEGA'] = k
k += 1    
featureTable['word-UNK'] = k
k += 1
featureTable['prev-word-UNK'] = k
k += 1
featureTable['next-word-UNK'] = k
k += 1

for key in trainPOS:
    pos = "-".join(['pos',key])
    featureTable[pos] = k
    k += 1
    prevPOS = "-".join(['prev-pos',key])
    featureTable[prevPOS] = k
    k += 1
    nextPOS = "-".join(['next-pos',key])
    featureTable[nextPOS] = k
    k += 1


featureTable['prev-pos-PHIPOS'] = k
k += 1
#featureTable['prev PHI'] = k
#k += 1
featureTable['next-pos-OMEGAPOS'] = k
k += 1    
featureTable['pos-UNK'] = k
k += 1
featureTable['prev-pos-UNK'] = k
k += 1
featureTable['next-pos-UNK'] = k
k += 1


binaryFeatures = ['ABBR','CAP','LOC']    
for feat in binaryFeatures:
    featureTable[feat] = k
    k += 1



labelDict = {}
labelDict['O'] = 0
labelDict['B-PER'] = 1
labelDict['I-PER'] = 2
labelDict['B-LOC'] = 3
labelDict['I-LOC'] = 4
labelDict['B-ORG'] = 5
labelDict['I-ORG'] = 6


    
for i in range(trainlength):
#for i in range(50):    
    line = trainSplitOnLine[i].split()
    if i < (trainlength-1):
        nextline = trainSplitOnLine[i+1].split()
    WORDCON = ['','']
    POSCON = ['','']
    if i == 0:        
        if len(line) != 0:                    
            WORD = line[-1]            
            label = labelDict[line[0]]
            POS = line[1]
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
            label = labelDict[line[0]]
            WORD = line[-1]             
            POS = line[1]
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
        word = "-".join(['word',WORD])
        pos = "-".join(['pos', POS])
        prevword = "-".join(['prev-word',WORDCON[0]])
        nxtword = "-".join(['next-word',WORDCON[1]])
        prevpos = "-".join(['prev-pos',POSCON[0]])
        nxtpos = "-".join(['next-pos',POSCON[1]])
        abbreviation = ABBR
        capitalized = CAP
        location = LOC
        
        vec = []   
        auxVec = []
        fidword = ":".join([str(featureTable[word]),'1'])
        auxVec.append(featureTable[word])
        fidprevword = ":".join([str(featureTable[prevword]),'1'])
        auxVec.append(featureTable[prevword])
        fidnextword = ":".join([str(featureTable[nxtword]),'1'])
        auxVec.append(featureTable[nxtword])
        fidpos = ":".join([str(featureTable[pos]),'1'])
        auxVec.append(featureTable[pos])
        fidprevpos = ":".join([str(featureTable[prevpos]),'1'])
        auxVec.append(featureTable[prevpos])
        fidnxtpos = ":".join([str(featureTable[nxtpos]),'1'])
        auxVec.append(featureTable[nxtpos])
        fidABBR = ":".join([str(featureTable['ABBR']),'1'])
        auxVec.append(featureTable['ABBR'])
        fidCAP = ":".join([str(featureTable['CAP']),'1'])
        auxVec.append(featureTable['CAP'])
        fidLOC = ":".join([str(featureTable['LOC']),'1'])
        auxVec.append(featureTable['LOC'])
        auxVec.sort()        
        anotherVec = []
        for item in auxVec:
            anotherVec.append(":".join([str(item),'1']))
        
        vec = [label]
        finalVec = [label]
        if 'WORD' in possibleFtype:
            vec.append(fidword)
        if 'WORDCON' in possibleFtype:
            vec.append(fidprevword)
            vec.append(fidnextword)
        if 'POSCON' in possibleFtype:
            vec.append(fidprevpos)
            vec.append(fidnxtpos)
        if 'POS' in possibleFtype:
            vec.append(fidpos)
        if 'ABBR' in possibleFtype:
            if abbreviation == 'yes':                
                vec.append(fidABBR)
        if 'CAP' in possibleFtype:
            if capitalized == 'yes':                
                vec.append(fidCAP)
        if 'LOCATION' in possibleFtype:
            if location == 'yes':                
                vec.append(fidLOC)        
        #print(*vec, sep = ' ')
        for feat in anotherVec:
            if feat in vec:
                finalVec.append(feat)
        #print(*vec, sep = ' ')                
        out33.write(" ".join([str(finalVec[0])," ".join(finalVec[1:])]))        
        #out33.write(" ".join([str(vec[0])," ".join(vec[1:])]))
        out33.write('\n')
out33.close()        
        
for i in range(testlength):
#for i in range(50):    
    line = testSplitOnLine[i].split()
    if i < (testlength-1):
        nextline = testSplitOnLine[i+1].split()
    WORDCON = ['','']
    POSCON = ['','']
    if i == 0:        
        if len(line) != 0:                    
            WORD = line[-1]
            auxWORD = WORD
            if WORD in trainWords:
                WORD = line[-1]                
            else:
                WORD = 'UNK'            
            label = labelDict[line[0]]
            POS = line[1]
            if POS in trainPOS:
                POS = line[1]
            else:
                POS = 'UNKPOS'             
            ABBR = isABBR(auxWORD)                
            CAP = isCAP(auxWORD)            
            LOC = isLOC(auxWORD)
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
            label = labelDict[line[0]]
            WORD = line[-1]
            auxWORD = WORD
            if WORD in trainWords:
                WORD = line[-1]                
            else:
                WORD = 'UNK'            
            label = labelDict[line[0]]
            POS = line[1]
            if POS in trainPOS:
                POS = line[1]
            else:
                POS = 'UNKPOS'             
            ABBR = isABBR(auxWORD)                
            CAP = isCAP(auxWORD)            
            LOC = isLOC(auxWORD)
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
        word = "-".join(['word',WORD])
        pos = "-".join(['pos', POS])
        prevword = "-".join(['prev-word',WORDCON[0]])
        nxtword = "-".join(['next-word',WORDCON[1]])
        prevpos = "-".join(['prev-pos',POSCON[0]])
        nxtpos = "-".join(['next-pos',POSCON[1]])
        abbreviation = ABBR
        capitalized = CAP
        location = LOC
        
        vec = []   
        auxVec = []
        fidword = ":".join([str(featureTable[word]),'1'])
        auxVec.append(featureTable[word])
        fidprevword = ":".join([str(featureTable[prevword]),'1'])
        auxVec.append(featureTable[prevword])
        fidnextword = ":".join([str(featureTable[nxtword]),'1'])
        auxVec.append(featureTable[nxtword])
        fidpos = ":".join([str(featureTable[pos]),'1'])
        auxVec.append(featureTable[pos])
        fidprevpos = ":".join([str(featureTable[prevpos]),'1'])
        auxVec.append(featureTable[prevpos])
        fidnxtpos = ":".join([str(featureTable[nxtpos]),'1'])
        auxVec.append(featureTable[nxtpos])
        fidABBR = ":".join([str(featureTable['ABBR']),'1'])
        auxVec.append(featureTable['ABBR'])
        fidCAP = ":".join([str(featureTable['CAP']),'1'])
        auxVec.append(featureTable['CAP'])
        fidLOC = ":".join([str(featureTable['LOC']),'1'])
        auxVec.append(featureTable['LOC'])
        auxVec.sort()
        anotherVec = []
        for item in auxVec:
            anotherVec.append(":".join([str(item),'1']))
        finalVec = [label]
        vec = [label]
        if 'WORD' in possibleFtype:
            vec.append(fidword)
        if 'WORDCON' in possibleFtype:
            vec.append(fidprevword)
            vec.append(fidnextword)
        if 'POSCON' in possibleFtype:
            vec.append(fidprevpos)
            vec.append(fidnxtpos)
        if 'POS' in possibleFtype:
            vec.append(fidpos)
        if 'ABBR' in possibleFtype:
            if abbreviation == 'yes':                
                vec.append(fidABBR)
        if 'CAP' in possibleFtype:
            if capitalized == 'yes':                
                vec.append(fidCAP)
        if 'LOCATION' in possibleFtype:
            if location == 'yes':                
                vec.append(fidLOC)
        for feat in anotherVec:
            if feat in vec:
                finalVec.append(feat)
        #print(*vec, sep = ' ')        
        #out44.write(" ".join([str(vec[0])," ".join(vec[1:])]))        
        out44.write(" ".join([str(finalVec[0])," ".join(finalVec[1:])]))        
        out44.write('\n')
out44.close()                                                            

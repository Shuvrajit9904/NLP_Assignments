import sys


#file1 = open('eval-program-files/prediction.txt')
file1 = open(sys.argv[1])
#file2 = open('eval-program-files/gold.txt')
file2 = open(sys.argv[2])

trainRaw = file1.read()
goldRaw = file2.read()

train = trainRaw.split('\n')
gold = goldRaw.split('\n')

person = {}
organisation = {}


def findNER(data, B, I):
    out = []
    for i in range(len(data)):
        lineSp = data[i].split()
        if len(lineSp) > 0:            
            label = lineSp[0]
            word = lineSp[-1]
            if label == B:
                ner = []
                flag = 1
                ner.append(word)
                startind = i+1
                ind = i+1
                while(flag == 1 and ind < len(data)):                    
                    linesp = data[ind].split()
                    if len(linesp) > 0:
                        label1 = linesp[0]
                        if label1 == I:
                            ner.append(linesp[-1])
                        else:
                            flag = 0
                    else:
                        flag = 0
                        break
                    ind += 1
                endind = ind - 1
                nerOnly = " ".join(ner)
                indOnly = "".join(['[',str(startind),'-',str(endind),']'])
                nerWind = " ".join([nerOnly,indOnly])
                out.append(nerWind)
    return out

tst = findNER(train[:100], 'B-PER', 'I-PER')
for items in tst:
    print items
'''
#LOCATION
loc = findNER(train, 'B-LOC', 'I-LOC')
locG = findNER(gold, 'B-LOC', 'I-LOC')
correctLoc = []
correctL = 0
for item in loc:
    if item in locG:
        correctLoc.append(item)
        correctL += 1
numerL = correctL
denomPreL = len(loc)
denomRecL = len(locG)

print "Correct LOC =", ",".join(correctLoc)
print "Precision LOC =", "".join([str(numerL),'/',str(denomPreL)])
print "Recall LOC =", "".join([str(numerL),'/',str(denomRecL)])
print '\n'

#PERSON
per = findNER(train, 'B-PER', 'I-PER')
perG = findNER(gold, 'B-PER', 'I-PER')
correctPer = []
correctP = 0
for item in per:
    if item in perG:
        correctPer.append(item)
        correctP += 1
numerP = correctP
denomPreP = len(per)
denomRecP = len(perG)

if len(correctPer) != 0:
    print "Correct PER =", " | ".join(correctPer)
else:
    print "Correct PER = NONE"
if denomPreP != 0:
    print "Precision PER =", "".join([str(numerP),'/',str(denomPreP)])
else:
    print "Precision PER = n/a"
if denomRecP != 0:
    print "Recall PER =", "".join([str(numerP),'/',str(denomRecP)])
else:
    print "Recall PER = n/a"
print '\n'

#ORGANISATION
org = findNER(train, 'B-ORG', 'I-ORG')
orgG = findNER(gold, 'B-ORG', 'I-ORG')
correctOrg = []
correctO = 0
for item in org:
    if item in orgG:
        correctOrg.append(item)
        correctO += 1
numerO = correctO
denomPreO = len(org)
denomRecO = len(orgG)

print "Correct ORG =", ",".join(correctOrg)
print "Precision ORG =", "".join([str(numerO),'/',str(denomPreO)])
print "Recall ORG =", "".join([str(numerO),'/',str(denomRecO)])
print '\n'

'''

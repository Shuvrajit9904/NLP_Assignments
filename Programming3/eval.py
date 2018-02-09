import sys


#file1 = open('eval-program-files/prediction.txt')
file1 = open(sys.argv[1])
#file2 = open('eval-program-files/gold.txt')
file2 = open(sys.argv[2])

trainRaw = file1.read()
goldRaw = file2.read()

outputfile = 'eval.txt'
outfile = open(outputfile, "w")

train = trainRaw.split('\n')
gold = goldRaw.split('\n')

person = {}
organisation = {}


def findNER(data, B, I):
    out = []
    for i in range(len(data)):
        lineSp = data[i].split()
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
                label1 = linesp[0]
                if label1 == I:
                    ner.append(linesp[-1])
                else:
                    flag = 0
                ind += 1
            endind = ind - 1
            nerOnly = " ".join(ner)
            indOnly = "".join(['[',str(startind),'-',str(endind),']'])
            nerWind = " ".join([nerOnly,indOnly])
            out.append(nerWind)
    return out



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
    #print "Correct PER =", " | ".join(correctPer)
    outfile.write("Correct PER = {}".format(" | ".join(correctPer)))
    outfile.write('\n')
else:
    #print "Correct PER = NONE"
    outfile.write("Correct PER = NONE")
    outfile.write('\n')
if denomRecP != 0:
    #print "Recall PER =", "".join([str(numerP),'/',str(denomRecP)])
    outfile.write("Recall PER = {}".format("".join([str(numerP),'/',str(denomRecP)])))
    outfile.write('\n')
else:
    #print "Recall PER = n/a"
    outfile.write("Recall PER = n/a")
    outfile.write('\n')
if denomPreP != 0:
    #print "Precision PER =", "".join([str(numerP),'/',str(denomPreP)])
    outfile.write("Precision PER = {}".format("".join([str(numerP),'/',str(denomPreP)])))
    outfile.write('\n')
else:
    #print "Precision PER = n/a"
    outfile.write("Precision PER = n/a")
    outfile.write('\n')
#print '\n'
outfile.write('\n')


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
if len(correctLoc) != 0:
    #print "Correct LOC =", "|".join(correctLoc)
    outfile.write("Correct LOC = {}".format(" | ".join(correctLoc)))
    outfile.write('\n')
else:
    #print "Correct LOC = NONE"
    outfile.write('Correct LOC = NONE')
    outfile.write('\n')
if denomRecL != 0:
    #print "Recall LOC =", "".join([str(numerL),'/',str(denomRecL)])
    outfile.write("Recall LOC = {}".format("".join([str(numerL),'/',str(denomRecL)])))
    outfile.write('\n')
else:
    #print "Recall LOC = n/a"    
    outfile.write("Recall LOC = n/a")
    outfile.write('\n')
if denomPreL != 0:
    #print "Precision LOC =", "".join([str(numerL),'/',str(denomPreL)])
    outfile.write("Precision LOC = {}".format("".join([str(numerL),'/',str(denomPreL)])))
    outfile.write('\n')
else:
    #print "Precision LOC = n/a"
    outfile.write("Precision LOC = n/a")
    outfile.write('\n')
#print '\n'
outfile.write('\n')


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

if len(correctOrg) != 0:
    #print "Correct ORG =", "|".join(correctOrg)
    outfile.write("Correct ORG = {}".format(" | ".join(correctOrg)))
    outfile.write('\n')
else:
    #print "Correct ORG = NONE"
    outfile.write("Correct ORG = NONE")
    outfile.write('\n')
if denomRecO != 0:
    #print "Recall ORG =", "".join([str(numerO),'/',str(denomRecO)])
    outfile.write("Recall ORG =".format("".join([str(numerO),'/',str(denomRecO)])))
    outfile.write('\n')
else:
    #print "Recall ORG = n/a"
    outfile.write("Recall ORG = n/a")
    outfile.write('\n')
if denomPreO != 0:
    #print "Precision ORG =", "".join([str(numerO),'/',str(denomPreO)])
    outfile.write("Precision ORG = {}".format("".join([str(numerO),'/',str(denomPreO)])))
    outfile.write('\n')
else:
    #print "Precision ORG = n/a"
    outfile.write("Precision ORG = n/a")
    outfile.write('\n')    
#print '\n'
outfile.write('\n')

numer = numerL + numerP + numerO
preD = denomPreL + denomPreP + denomPreO
recD = denomRecL + denomRecP + denomRecO

if recD != 0:
    #print "Average Recall = {}/{}".format(numer, recD)
    outfile.write("Average Recall = {}/{}".format(numer, recD))
    outfile.write('\n')
else:
    #print "Average Recall = n/a"        
    outfile.write("Average Recall = n/a")
    outfile.write('\n')
if preD != 0:
    #print "Average Precision = {}/{}".format(numer, preD)
    outfile.write("Average Precision = {}/{}".format(numer, preD))
    outfile.write('\n')
else:
    #print "Average Precision = n/a"
    outfile.write("Average Precision = n/a")
    outfile.write('\n')
outfile.close()

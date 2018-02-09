import math
from collections import Counter
#Input
openCorp = open('train.txt')
phicount = 0
wordcount = 0
unigramsize = 0

freqUni ={}
freqBi ={}
freqSm = {}
probUni ={}
probBi = {}
probSm = {}
biGram = []
#Unigrams
'''for line in openCorp:
    ln = line.strip('\n')
    nline = ln.strip().split()
    #print nline
    for w in xrange(len(nline)):
        word = nline[w]
        unigramsize = unigramsize + 1
        nwrd = word.lower()
        if nwrd in freqUni:
            freqUni[nwrd] = freqUni[nwrd] + 1
        else:
            freqUni[nwrd] =  1
    #for i in range(len(nline)):    
        if w == 0:
            bigram = " ".join(['phi',nline[w].lower()])                                          
        else:
            bigram = " ".join([nline[w-1].lower(),nline[w].lower()])
        #print bigram
        #freqBi = Counter(bigram)
        #if bigram in freqBi:
        #    freqBi[bigram] = freqBi[bigram] + 1
        #else:
        #    freqBi[bigram] = 1
        biGram.append(bigram)
'''
#Unigrams
unigrams = []
sentences = []
for line in openCorp:
    ln = line.strip('\n')
    nline = ln.strip().split()
    unigramsize = unigramsize + len(nline)
    sentences.append(nline)
    phicount = phicount + 1

freqUni = Counter([word.lower() for line in sentences for word in line])
for key in freqUni:
    prob = float(freqUni[key])/ unigramsize
    probUni[key] = math.log(prob,2)

print unigramsize

#Smoothing
vocab = len(freqUni)
factor = float(unigramsize)/(vocab+unigramsize) # Multiplication factor to accomodate smoothing

#Bigrams
openCorp = open('train.txt')
bigrams = []
for line in openCorp:
    ln = line.strip('\n')
    nline = ln.strip().split()
    #nline = wline.insert
    for i in range(len(nline)-1):
        if i != 0:
            bigrams.append(' '.join([nline[i-1].lower(), nline[i].lower()]))
        else:
            #phicount = phicount + 1
            bigrams.append(' '.join(['phi', nline[i].lower()]))

freqBi = Counter(bigrams)

#Smoothing
for keyB in freqBi:
    freqSm[keyB] = (freqBi[keyB]+1)*factor
    denom = keyB.split()    
    denomB = denom[0]
    if denomB != 'phi':
        probB = float(freqBi[keyB])/freqUni[denomB]
        probsm = float(freqBi[keyB]+1)/(freqUni[denomB]+vocab+1)
    else:
        probB = float(freqBi[keyB])/phicount
        probsm = float(freqBi[keyB]+1)/(phicount+vocab+1)
        
    probBi[keyB] = math.log(probB,2)    
    probSm[keyB] = math.log(probsm,2)

S = 'But old Mr. Toad will leave one day .'
s = S.strip().split(' ')
logprobUni = 0
logprobBi = 0
logprobSm = 0

for w in s:
    logprobUni = logprobUni + probUni[w.lower()]    

for wb in range(len(s)):
    if wb == 0:
        bigramT = " ".join(['phi',s[wb].lower()])
    else:
        bigramT = " ".join([s[wb-1].lower(),s[wb].lower()])
    if bigramT in freqBi:        
        logprobBi = logprobBi + probBi[bigramT]
    else:
        logprobBi = 'Undefined'
        break

for wb1 in range(len(s)):    
    if wb1 == 0:
        bigramS = " ".join(['phi',s[wb1].lower()])
    else:
        bigramS = " ".join([s[wb1-1].lower(),s[wb1].lower()])    
    if bigramS in freqBi:                
        logprobSm = logprobSm + probSm[bigramS]        
    else:
        if wb1 == 0:
            print "here1"
            unseenprob = float(1)/(vocab+phicount+1)            
        else:
            unseenprob = float(1)/(freqUni[s[wb1-1].lower()]+vocab+1)
        logprobSm = logprobSm + math.log(unseenprob,2)    

    
print logprobUni
print logprobBi
print logprobSm


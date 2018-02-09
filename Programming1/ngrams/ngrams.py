import sys
import math
from collections import Counter
import random
#Input
file1 = sys.argv[1]
file2 = sys.argv[3]
funct = sys.argv[2]

#Input

def generator(seed, freqBi, count, snttry):    
    count = count + 1
    tempdict = {}
    fsum = 0
    for k in freqBi:
        k1 = k.split()
        word = k1[0]
        if seed.lower() == word.lower():
            tempdict[k] = freqBi[k]    
    for k2 in tempdict:
        fsum = fsum + tempdict[k2]
    for k3 in tempdict:
        tempdict[k3] = (float(tempdict[k3])/fsum)*100    
    dist = 100    
    minkey = None
    #while (minkey == None):
    rand1 = random.randint(0,100)
    rand = float(rand1)/100    
    for k4 in tempdict:
        last = k4
        if abs(tempdict[k4]-rand) < dist:
            dist = abs(tempdict[k4]-rand)
            minkey = k4
    if minkey != None:
        nxt = minkey.split()    
        nxtseed = nxt[-1]    
        snttry.append(nxtseed)
        if nxtseed in ('.','?','!') or count >=10:
            return nxtseed
        else:        
            wrd = generator(nxtseed, freqBi, count, snttry)

    smthng = " ".join(snttry)
    return smthng


if funct == '-test':
    openCorp = open(file1)
    phicount = 0
    wordcount = 0
    unigramsize = 0

    freqUni ={}
    freqBi = {}
    freqSm = {}
    probUni = {}
    probBi = {}
    probSm = {}
    biGram = []

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
        for i in range(len(nline)):
            if i != 0:
                bigrams.append(' '.join([nline[i-1].lower(), nline[i].lower()]))
            else:
                #phicount = phicount + 1
                bigrams.append(' '.join(['phi', nline[i].lower()]))

    freqBi = Counter(bigrams)

    #Smoothing
    for keyB in freqBi:
        #freqSm[keyB] = (freqBi[keyB]+1)*factor
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

    Stest = open('test.txt')
    for newsentence in Stest:
        print "S = " + newsentence
        s = newsentence.strip().split(' ')    
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
                    #print "here1"
                    unseenprob = float(1)/float(vocab+phicount+1)           
                else:
                    unseenprob = float(1)/float(freqUni[s[wb1-1].lower()] + vocab + 1)
                logprobSm = logprobSm + math.log(unseenprob,2)    
            

            
            
        print "Unsmoothed Unigrams, logprob(S) = ",round(logprobUni,4)
        if logprobBi != 'Undefined':
            print "Unsmoothed Bigrams, logprob(S) = ",round(logprobBi,4)
        else:
            print "Unsmoothed Bigrams, logprob(S) = ",logprobBi
        print "Smoothed Bigrams, logprob(S) = ",round(logprobSm,4)
        print '\n'


elif funct == '-gen':
    openCorp = open(file1)
    phicount = 0
    wordcount = 0
    unigramsize = 0

    freqUni ={}
    freqBi = {}
    freqSm = {}
    probUni = {}
    probBi = {}
    probSm = {}
    biGram = []

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

    #print unigramsize

    #Smoothing
    vocab = len(freqUni)
    factor = float(unigramsize)/(vocab+unigramsize) # Multiplication factor to accomodate smoothing

    #Bigrams
    openCorp = open(file1)
    bigrams = []
    for line in openCorp:
        ln = line.strip('\n')
        nline = ln.strip().split()
        #nline = wline.insert
        for i in range(len(nline)):
            if i != 0:
                bigrams.append(' '.join([nline[i-1].lower(), nline[i].lower()]))
            else:
                #phicount = phicount + 1
                bigrams.append(' '.join(['phi', nline[i].lower()]))

    freqBi = Counter(bigrams)

    #Smoothing
    for keyB in freqBi:
        #freqSm[keyB] = (freqBi[keyB]+1)*factor
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

    Stest = open('test.txt')
    for newsentence in Stest:
        #print "S = " + newsentence
        s = newsentence.strip().split(' ')    
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
                    #print "here1"
                    unseenprob = float(1)/float(vocab+phicount+1)           
                else:
                    unseenprob = float(1)/float(freqUni[s[wb1-1].lower()] + vocab + 1)
                logprobSm = logprobSm + math.log(unseenprob,2)                
    gen = open(file2)
    for seedi in gen:    
        seed = seedi.strip()
        print "Seed = ", seed
        print '\n'
        for it in range(10):
            sent = [seed]
            sent.append(generator(seed, freqBi, count=0, snttry = []))
            print "Sentence {}: {}".format((it+1)," ".join(sent))
        print '\n'

else:
    print "Incorrect input.Please try again."
    sys.exit()

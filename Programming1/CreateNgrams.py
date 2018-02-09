import math

#Input
openCorp = open('train.txt')
corp = openCorp.read()
splitCorp = corp.strip().split('\n')
phicount = len(splitCorp)

# Corpsize is count of words in the corpus
corptoken = corp.strip().split(' ')
corpsize = len(corptoken)

freqUni = {} #Frequency Count for Unigrams
probUni = {} #Probability of Unigrams
freqBi = {} #Frequency Count for Bigrams
probBi = {} #Probability of Bigrams
freqBiSmooth = {}
probBiSmooth = {}

vocab = len(freqUni)
factor = float(corpsize)/(vocab+corpsize) # Multiplication factor to accomodate smoothing

# Frequency and Probability Calculation
for line in splitCorp:
    corpToken = line.strip().split(' ')
    # For each word in each line count the number of appearence 
    for tokenD in corpToken:        
        token = tokenD.lower()        # Lowercase all strings to make it case insensitive
        if token in freqUni:
            freqUni[token] = freqUni[token]+1
        else:
            freqUni[token] = 1

    # Frequency and Probability calculation for Bigrams
    for i in range(len(corpToken)):
        if i == 0:    
            bigram = " ".join(['phi',corpToken[i].lower()])           
        else:
            bigram = " ".join([corpToken[i-1].lower(), corpToken[i].lower()])
        # Instead of concatenated text, saving the bigram as a hash result        
        if bigram in freqBi:
            freqBi[bigram] = freqBi[bigram] + 1
            freqBiSmooth[bigram] = (freqBi[bigram]+1) * factor            
                
        else:
            freqBi[bigram] = 1
            freqBiSmooth[bigram] = (freqBi[bigram]+1) * factor
            
#Converting probability to Log(base 2) scale
for key in freqUni:        
    prob = float(freqUni[key])/corpsize    
    probUni[key] = math.log(prob,2)

for keyBi in freqBi:
    divd = keyBi.split(' ')
    denom = divd[0]
    if denom != 'phi':
        prob = float(freqBi[keyBi])/freqUni[denom]
        probBi[keyBi] = math.log(prob,2)    

Sentence = 'What could go wrong ?'
print Sentence
sen = Sentence.strip().split(' ')
prb = 0
for s in sen:
    w = s.lower()
    prb = prb + probUni[w]

print "Unsmoothed Unigrams, logprob(S) = ", prb

sent = Sentence.strip().split(' ')
biprob = 0
for j in range(len(sent)):    
    if j == 0:
        bigr = 'phi' + sent[j].lower()
    else:
        bigr = sent[j-1].lower() + sent[j].lower()    
    hf = bigr
    if hf in probBi:
        biprob = biprob + probBi[hf]
    else:
        biprob = 0
        break

print "Unsmoothed Bigrams, logprob(S) = ", biprob

#Read Test Data
testraw = open('test.txt')
testin = testraw.read()
test = testin.strip().split(' ')

#print factor

biprobsmth = 0
logprobOne = math.log(factor/corpsize, 2) # Frequency of a new word after smoothing
for j in range(len(sent)):    
    if j == 0:
        bigrm1 = " ".join(['phi', sent[j].lower()])
    else:
        bigrm1 = " ".join([sent[j-1].lower(), sent[j].lower()])
    hf = bigrm1
    if hf in probBi:
        biprobsmth = biprobsmth + probBiSmooth[hf]
    else:
        biprobsmth = biprobsmth + logprobOne

print "Smoothed Bigrams, logprob(S) = ", biprobsmth

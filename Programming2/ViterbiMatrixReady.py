import numpy as np
import math
prob = open('probs.txt')
probDict = {}
for items in prob:
    split1 = items.split()
    ky = " ".join([split1[0],split1[1]])
    probDict[ky] = float(split1[-1])

sent = open('sents.txt')
pos = open('possiblePoS.txt')
possiblePoS = []

for line in pos:
    line.strip('\n')
    possiblePoS.append(line.strip('\n'))

dictPoS = {}
for i in range(len(possiblePoS)):
    dictPoS[i] = possiblePoS[i]
    
for line in sent:    
    split2 = line.split()
    l1 = len(split2)
    l2 = len(possiblePoS)
    viterbi = np.ones((l2, l1))
    for wrd in range(l1):
        for state in range(l2):
            if wrd == 0:
                transition = " ".join([possiblePoS[state].lower(),'phi'])
                emission = " ".join([split2[wrd],possiblePoS[state]])                            
                if emission and transition in probDict:
                    viterbi[state,wrd] = probDict[transition]*probDict[emission]
                elif emission in probDict and transition not in probDict:
                    viterbi[state,wrd] = math.pow(10,-4)*probDict[emission]
                elif transition in probDict and emission not in probDict:
                    viterbi[state,wrd] = math.pow(10,-4)*probDict[transition]
                else:
                    viterbi[state,wrd] = math.pow(10,-8)
            else:                
                emission = " ".join([split2[wrd].lower(),possiblePoS[state].lower()])                
                maintainarray = []
                i = 0
                for st in viterbi[:,wrd-1]:
                    transition = " ".join([possiblePoS[state], dictPoS[i]])
                    if transition in probDict:                            
                        maintainarray.append(st * probDict[transition])
                    else:
                        maintainarray.append(st * 0.0001)
                    i += 1
                if emission in probDict:                    
                    viterbi[state,wrd] = max(maintainarray)*probDict[emission]
                else:
                    viterbi[state,wrd] = max(maintainarray)*math.pow(10,-4)

    v = np.log2(viterbi)
    print v

import sys
from math import log
from collections import Counter
import random
random.seed(9001)

def test(f1, f2):
	train_unigram = []
	with open(f1, 'r') as train:
		train_unigram = [line.rstrip().split() for line in train]    
	test_unigram = []
	with open(f2, 'r') as test:
		test_unigram = [line.rstrip().split() for line in test]
	unigrams = Counter([word.lower() for sentence in train_unigram for word in sentence])
	total_unigrams = len([word.lower() for sentence in train_unigram for word in sentence])
	unsmoothed_unigram_probabilities = un_uni_prob (unigrams, total_unigrams, test_unigram)
	train_bigram = []
	with open(f1, 'r') as train:
		train_bigram = [['phi'] + line.rstrip().split() for line in train]    
	test_bigram = []
	with open(f2, 'r') as test:
		test_bigram = [['phi'] + line.rstrip().split() for line in test]
	bigram_list = []
	for S in train_bigram:
		S = map(lambda x: x.lower(), S)
		for i in range(len(S) - 1):
			bigram_list.append(' '.join([S[i], S[i + 1]]))
	bigrams = Counter(bigram_list)
	total_bigrams = len(bigram_list)
	unsmoothed_bigram_probabilities = un_bi_prob (bigrams, test_bigram)
	smoothed_bigram_probabilities = s_bi_prob (unigrams, bigrams, test_bigram)
	for i in range(len(test_unigram)):
		print 'S =', ' '.join(test_unigram[i]), '\n'
		print 'Unsmoothed Unigrams, logprob(S) =', unsmoothed_unigram_probabilities[i]
		if float(unsmoothed_bigram_probabilities[i]) == 0.0:
			print 'Unsmoothed Bigrams, logprob(S) = undefined'
		else:
			print 'Unsmoothed Bigrams, logprob(S) =', unsmoothed_bigram_probabilities[i]
		print 'Smoothed Bigrams, logprob(S) =', smoothed_bigram_probabilities[i], '\n\n'

def un_uni_prob (unigrams, total_unigrams, test_unigram):
	unsmoothed_unigram_probabilities = []
	for S in test_unigram:
		p = 0
		for i in range(len(S)):
			u = S[i].lower()
			if u in unigrams.keys():
				p += log(unigrams[u]/float(total_unigrams), 2)
		unsmoothed_unigram_probabilities.append("%.4f" % p)
	return unsmoothed_unigram_probabilities

def un_bi_prob (bigrams, test_bigram):
	unsmoothed_bigram_probabilities = []
	for S in test_bigram:
		p = 0
		for i in range(len(S)-1):
			b = S[i].lower() + ' ' + S[i+1].lower()
			if b in bigrams.keys():
				p += log(bigrams[b]*1.0/(bigrams_start_with(b.split()[0], bigrams)), 2)
			else:
				p = 0.0000
				break
		unsmoothed_bigram_probabilities.append("%.4f" % p)
	return unsmoothed_bigram_probabilities

def s_bi_prob(unigrams, bigrams, test_bigram):
	vocabulary = len(unigrams.keys()) + 1
	smoothed_bigram_probabilities = []
	for S in test_bigram:
		p = 0
		for i in range(len(S)-1):
			b = S[i].lower() + ' ' + S[i+1].lower()
			if b in bigrams.keys():
				p += log((bigrams[b]+ 1)*1.0/(bigrams_start_with(S[i].lower(), bigrams) + vocabulary), 2)
			else:
				p += log(1.0/(bigrams_start_with(S[i].lower(), bigrams) + vocabulary), 2)
		smoothed_bigram_probabilities.append("%.4f" % p)
	return smoothed_bigram_probabilities

def bigrams_start_with(word, bigrams):
	return sum([bigrams[x] for x in bigrams.keys() if x.startswith(word + " ")])

def gen(f1, f2):
	train_bigram = []
	with open(f1, 'r') as train:
		train_bigram = [['phi'] + line.rstrip().split() for line in train]
	bigram_list = []
	for S in train_bigram:
		S = map(lambda x: x.lower(), S)
		for i in range(len(S) - 1):
			bigram_list.append(' '.join([S[i], S[i + 1]]))
	bigrams = Counter(bigram_list)
	total_bigrams = len(bigram_list)

	seeds = []
	with open(f2, 'r') as s:
		seeds = [line.rstrip() for line in s]
	for seed in seeds:
		generator (seed, bigrams)
		print

def generator(init_seed, bigrams):
	print 'Seed = ', init_seed, '\n'	
	sentence = init_seed
	for i in range(1,11):
		sentence = init_seed
		seed = init_seed.lower()
		while (True):
			if seed == '.' or seed == '?' or seed == '!' or len(sentence.split()) == 11:
				break
			b_seed = [x for x in bigrams.keys() if x.startswith(seed + " ")]
			freq = [bigrams[x] for x in bigrams.keys() if x.startswith(seed + " ")]
			p = [log(f/float(len(freq)),2) for f in freq]
			sortedb = [x for _,x in sorted(zip(p, b_seed))]
			freq = sorted(freq)
			r = random.random()
			if r != 0:
				r = log(r, 2)
			next_id = len(freq)-1
			for f in range(len(freq)):
				if p[f] >= r:
					next_id = f
			if b_seed == []:
				break
			else:
				next_bigram = b_seed[next_id]
			sentence = sentence + " " + next_bigram.split()[1]
			seed = next_bigram.split()[1]
		print 'Sentence ', i, '=', sentence


if len(sys.argv) < 4:
	print "Incorrect input. Please try again."
	sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[3]
function = sys.argv[2]

if function == '-test':
	test(file1, file2)
elif function == '-gen':
	gen(file1, file2)
else:
	print "Incorrect input. Please try again."
	sys.exit()

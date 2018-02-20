# Viterbi Algorithm

import numpy as np
from nltk.tokenize import word_tokenize
from data import bigram, lexical, pos_dict, word_dict, NUM_TAGS

sent = input("Enter the sentence : ")
words = word_tokenize(sent)
NUM_UNIQUE_WORDS = len(np.unique(words))
NUM_WORDS = len(words)

# Algorithm
# Step 1 - Create a Matrix of appropriate size
w, h = NUM_WORDS, NUM_TAGS
Matrix = [[0 for x in range(w)] for y in range(h)]


# Step 2 - Initialize Matrix for first word
for i in range(NUM_TAGS):
	for w in word_dict:
		if w["name"] == words[0]:
			index = w["id"]
			break
	Matrix[i][0] = bigram[0][i] * lexical[index][i]


# Step 2.5 - Intialize pointers array
w, h = NUM_WORDS, NUM_TAGS
Pointers = [[0 for x in range(w)] for y in range(h)]


# Step 3 - Iteration to compute all values of Matrix
for j in range(1, NUM_WORDS):
	for i in range(NUM_TAGS):
		for w in word_dict:
			if w["name"] == words[j]:
				index = w["id"]
				break
		Matrix[i][j] = lexical[index][i] * max(x for x in [Matrix[k][j-1] * bigram[k+1][i] for k in range(NUM_TAGS)])
		ptr = [x for x in [Matrix[k][j-1] * bigram[k+1][i] for k in range(NUM_TAGS)]]
		Pointers[i][j] = ptr.index(max(ptr))


# Step 4 - Find Maximum of last word column and backtrace
result = [0] * NUM_WORDS
last_pos = [x for x in [Matrix[k][NUM_WORDS-1] for k in range(NUM_TAGS)]]
result[0] = last_pos.index(max(last_pos))
t = result[0]

index = 1
for i in reversed(range(1, NUM_WORDS)):
	result[index] = Pointers[t][i]
	t = result[index]
	index += 1
final = list(reversed(result))


# Step 5 - Print final result
tags = []
for i in range(NUM_WORDS):
	for p in pos_dict:
		if p["id"] == final[i]:
			tags.append(p["name"])
			break
print("Tagged sentence : " + str(tags))

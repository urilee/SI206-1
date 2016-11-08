# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text


print("START*******")
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random
from nltk import word_tokenize,sent_tokenize
from nltk.book import *


tokens = text2[0:150]
print("TOKENS")
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)
'''
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:150]:
		print (tup)
'''
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.10,"JJ":.10,"RB":.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


print ("The Original Text")
for word in tokens:
	print (spaced(word), end="")
print ("\n")

print ("New Madlib Text")
print ("".join(final_words))

print("\n\nEND*******")

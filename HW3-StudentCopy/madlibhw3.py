# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

# requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import nltk 
import random
from nltk import word_tokenize,sent_tokenize
from nltk.book import *


def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

print ("\n")		
print("START*******")

#first 150 tokens
tokens = text2[:150]
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

#original text
print ("\n")
print ("The Original Text")
for word in tokens:
	print (spaced(word), end="")
print ("\n")


tagmap = {"NN":"a noun","VBD":"past tense verbs","VB":"a verb","JJ":"an adjective", "RB":"an adverb"}
substitution_probabilities = {"NN":.15,"VBD":.10,"VB":.10,"JJ":.10,"RB":.10}

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


#new Madlib text
print ("\n")
print ("New Madlib Text")
print ("".join(final_words))

print("\n\nEND*******")

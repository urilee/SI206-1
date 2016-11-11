# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

subjectivity = 0.0
polarity = 0.0
totalsub = 0.0
totalpol = 0.0

#what to search for

public_tweets = api.search('minimal tattoos')

#gonna use this for demo
#public_tweets = api.search(input("Search Twitter: "))

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	subjectivity += analysis.sentiment.subjectivity
	polarity += analysis.sentiment.polarity
	totalsub += 1
	totalpol += 1

#subjectivity -- measures how factual
#polarity -- measures how positive or negative
print("Average subjectivity is " + str(subjectivity/totalsub))
print("Average polarity is " + str(polarity/totalpol))

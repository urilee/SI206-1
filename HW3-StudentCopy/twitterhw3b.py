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

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
avgsubjectivity = 0.0
avgpolarity = 0.0

public_tweets = api.search('minimal tattoos')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	avgsubjectivity += analysis.sentiment.subjectivity
	avgpolarity += analysis.sentiment.polarity


print("Average subjectivity is " + str(avgsubjectivity))
print("Average polarity is " + str(avgpolarity))

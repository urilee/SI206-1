# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#status and photo
twittermessage = "a picture from Copenhagen! #UMSI-206 #Proj3"
photofile = "Asset0011.jpg"

#upload image and message
api.update_with_media(photofile, twittermessage)

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")


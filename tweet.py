import tweepy
import os

# Load keys from environment
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Tweet text
tweet = "هنا تحط التغريدة الي تبغاها تظهر كل ساعتين"

api.update_status(tweet)
print("Tweet sent!")

import tweepy
import os

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweet_text = "مرحبا! هذا بوتي يشتغل كل ساعتين 🔥"

api.update_status(status=tweet_text)
print("Tweet sent!")

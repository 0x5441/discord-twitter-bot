import requests
import os
import base64

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Twitter token endpoint
token_url = "https://api.twitter.com/oauth2/token"

# Encode client_id:client_secret
key_secret = f"{client_id}:{client_secret}".encode("ascii")
b64_encoded_key = base64.b64encode(key_secret).decode("ascii")

headers = {
    "Authorization": f"Basic {b64_encoded_key}",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
}

data = {"grant_type": "client_credentials"}

# Get bearer token
response = requests.post(token_url, headers=headers, data=data)
access_token = response.json().get("access_token")

# Tweet endpoint
tweet_url = "https://api.twitter.com/2/tweets"

tweet_text = "تغريدتك هنا يا سلطان كل ساعتين"

tweet_payload = {"text": tweet_text}

tweet_headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

tweet_response = requests.post(tweet_url, headers=tweet_headers, json=tweet_payload)

print(tweet_response.status_code)
print(tweet_response.text)

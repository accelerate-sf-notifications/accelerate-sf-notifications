import sys
sys.path.append('../../')
import config

import requests
from requests_oauthlib import OAuth1

# Replace the following variables with your own credentials
API_KEY = config.vars["x-twitter"]["api_key"]
API_SECRET_KEY = config.vars["x-twitter"]["api_secret_key"]
ACCESS_TOKEN = config.vars["x-twitter"]["access_token"]  # Make sure this is the new token
ACCESS_TOKEN_SECRET = config.vars["x-twitter"]["access_token_secret"]  # Make sure this is the new token secret

# The URL for the Create Tweet endpoint
CREATE_TWEET_URL = config.vars["x-twitter"]["create_tweet_url"]

# The tweet text
tweet_text = config.vars["x-twitter"]["tweet_text"]

# OAuth 1 Authentication
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# The payload of our tweet
payload = {
    'text': tweet_text
}

# Making the POST request to the Twitter API to create a tweet
response = requests.post(CREATE_TWEET_URL, json=payload, auth=auth)

# Checking if the request was successful
if response.status_code == 201:
    print('Successfully created tweet.')
    print('Tweet ID:', response.json()['data']['id'])
else:
    print('Could not create tweet.')
    print('Response:', response.status_code, response.json())

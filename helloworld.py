#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import tweepy
from tweepy.error import TweepError
import time
import random
import string
import sys

import KEYS_AND_TOKENS

argfile = str(sys.argv[1])

CONSUMER_KEY = KEYS_AND_TOKENS.CONSUMER_KEY
CONSUMER_SECRET = KEYS_AND_TOKENS.CONSUMER_SECRET
ACCESS_KEY = KEYS_AND_TOKENS.ACCESS_KEY
ACCESS_SECRET = KEYS_AND_TOKENS.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    try:
        message = '{}\n({})'.format(line, datetime.now())
        api.update_status(message)
        print(message)
    except TweepError:
        print('pass')
        pass
    time.sleep(60)

# for tweet in tweepy.Cursor(api.search, q='#bonsai', lang='en').items(10):
    # print(tweet.text)
# print(api.rate_limit_status())



# def mock_tweet():
#     count = random.randint(50, 200)
#     return ''.join([random.choice(string.ascii_letters for _ in range(count))])

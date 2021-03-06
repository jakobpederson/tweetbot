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

# argfile = str(sys.argv[1])

CONSUMER_KEY = KEYS_AND_TOKENS.CONSUMER_KEY
CONSUMER_SECRET = KEYS_AND_TOKENS.CONSUMER_SECRET
ACCESS_KEY = KEYS_AND_TOKENS.ACCESS_KEY
ACCESS_SECRET = KEYS_AND_TOKENS.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# filename = open(argfile, 'r')
# f = filename.readlines()
# filename.close()

format = '%Y-%m-%d %H:%M'


def deck():
    cards = [
        'The Fool',
        'The Magician',
        'The High Priestess',
        'The Empress',
        'The Emperor',
        'The Hierophant',
        'The Lovers',
        'The Chariot',
        'Strength',
        'The Hermit',
        'Wheel of Fortune',
        'Justice',
        'The Hanged Man',
        'Death',
        'Temperance',
        'The Devil',
        'The Tower',
        'The Star',
        'The Moon',
        'The Sun',
        'Judgement',
        'The World',
        ]
    houses = ["Cups", "Wands", "Swords", "Pentacles"]
    royals = ["Ace", "Page", "Knight", "Queen", "King"]
    number_deck = []
    for house in houses:
        number_deck.extend(['{} of {}'.format(x, house) for x in list(range(2, 11))])
    for house in houses:
        number_deck.extend(['{} of {}'.format(x, house) for x in royals])
    cards.extend(number_deck)
    return cards

while(True):
    try:
        hand = random.sample(deck(), 3)
        final_hand = []
        for card in hand:
            orientation = random.sample(["", "Inverted"], 1)
            if orientation[0] == "Inverted":
                final_hand.append('{} ({})'.format(card, "Inverted"))
            else:
                final_hand.append('{}'.format(card))
        final_hand.append(datetime.now().strftime(format))
        message = '1.) {0}\n2.) {1}\n3.) {2}\n\n{3}'.format(*final_hand)
        api.update_status(message)
        print(message)
    except TweepError:
        print('pass')
        pass
    time.sleep(900)

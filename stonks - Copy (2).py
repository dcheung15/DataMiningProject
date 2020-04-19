#!/usr/bin/env python
# # Mining the Social Web, 3rd Edition
# ## Chapter 9: Twitter Cookbook
import sys
import time
import twitter
import json

def oauth_login():
    CONSUMER_KEY = '2ByXbf0TrOVmtfUOiAz6tjIb3'
    CONSUMER_SECRET='U3iY3sRMFdvjDUEroqKIFlUOfNnl1i20YKPMbuL6VBJ7MmuPvb'
    OAUTH_TOKEN='323221016-xHinePgz1ZLnYo8ph3fGg6zaVErXYNNDM1wMbO5r'
    OAUTH_TOKEN_SECRET='xqjvqPtblPRTynOb72Lv557FwzjymIB53ghM2qSJkFHCO'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                             CONSUMER_KEY,CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Sample usage
twitter_api = oauth_login()

# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print(twitter_api)


import sys
import twitter
#
## Query terms
#
q = '$JBLU'# Comma-separated list of terms
#
print('Filtering the public timeline for track={0}'.format(q), file=sys.stderr)
sys.stderr.flush()
#
## Returns an instance of twitter.Twitter
twitter_api = oauth_login()
#
## Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
#
## See https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data
stream = twitter_stream.statuses.filter(track=q)

# For illustrative purposes, when all else fails, search for Justin Bieber
# and something is sure to turn up (at least, on Twitter)

for tweet in stream:
    print(tweet['text'])
    sys.stdout.flush()


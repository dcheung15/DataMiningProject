#Final Project
#Senitiment Analysis

#imports needed
import twitter
from textblob import TextBlob
import datetime
import sys
import time
import json
import numpy as np
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt


# Your key here
key = '2Z7954OEL53VNE1Z'
ts = TimeSeries(key)
aapl, meta = ts.get_daily(symbol='AAPL')
print(aapl['2020-04-16'])

# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
aapl_data, aapl_meta_data = ts.get_intraday(symbol='AAPL', interval='5min')
# aapl_sma is a dict, aapl_meta_sma also a dict
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')

# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()


aapl_data
filewrite = open("AAPLApr15.txt", 'w')
#filewrite.write(aapl_data)
np.savetxt(r'c:\data\np.txt',aapl_data.get_values())
filewrite.close()

aapl_data.get_values


#Twitter Login
def oauth_login():
    CONSUMER_KEY = 'yYHRFNY1Bm8RXSHHhVf9QPDbA'
    CONSUMER_SECRET = 'Ok6PDfokRnxGlVgOtNJIZozXuOOuzSBrDerwA8o3bk1ED2Otx6'
    OAUTH_TOKEN = '1222252081064611846-Npx1OJC7juZZrKmIyMMGO6oDXJKzdb'
    OAUTH_TOKEN_SECRET = 'iPPC5gJzkqdN3457khiIOh37Mbt1fMlPeIFzkVQHmMege'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    return (twitter_api)

twitter_api = oauth_login()
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
print(twitter_api)

#
## Query terms
#
q = '$AAPL'# Comma-separated list of terms
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


company = '$AAPL'

#starting time
firstDT = datetime.datetime.now()
print("Start time:",str(firstDT))

#Starting point (company)
#company = '$AAL'

#>>>>>>> 5fe19e99151ad2fee515275c32bac649f06d072d
stream = twitter_stream.statuses.filter(track=company)

totalPolarity = 0
tweetsCounted = 0
    
for tweet in stream:
    tweetsCounted += 1
    text = tweet['text']
    print(text)
    blobText = TextBlob(text)
    polarity, subjectivity = blobText.sentiment
    totalPolarity += polarity
    if (tweetsCounted > 30):
        break

print("The total polarity of ", company, " is: ", totalPolarity)
if (totalPolarity > 0):
    print("Looks like the stock might go up today")
    print("Number of tweets: ", tweetsCounted)
if (totalPolarity < 0):
    print("Looks like the stock might go down today")
    print("Number of tweets: ", tweetsCounted)
if (totalPolarity == 0):
    print("Looks like the stock will stay the same same today")
    print("Number of tweets: ", tweetsCounted)

#trending words when stocks go negative/positive


#correlation


#end date time
lastDT = datetime.datetime.now()
print("End time:", str(lastDT))
print("Total Time:", str(lastDT-firstDT))

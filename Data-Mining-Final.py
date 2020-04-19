#Final Project
#Senitiment Analysis

#imports needed
import twitter
from textblob import TextBlob

def oauth_login():
    CONSUMER_KEY = 'FAJuwVnhJ1XR0mbkCdLfZB64x'
    CONSUMER_SECRET = 'wiB7VK2QATNxTCwRm0PWQhFm2MkNxWCDEdLfAy4jnNtDzzfPmH'
    OAUTH_TOKEN = '710158731-eaXDCt9V0JJGTWBrqikHGlyYIMuCaIhTLwaHicBn'
    OAUTH_TOKEN_SECRET = 'zNem0CaRPIpXOQFVJU88kwg0JiGFmWCIk8PKxKxqCWKdn'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    return (twitter_api)

twitter_api = oauth_login()
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
#Starting point (company)

company = '$AMZN'
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
    if (tweetsCounted > 15):
        break

print("The total polarity of ", company, " is: ", totalPolarity)
if (totalPolarity > 0):
    print("Looks like the stock might go up today")
if (totalPolarity < 0):
    print("Looks like the stock might go down today")
if (totalPolarity == 0):
    print("Looks like the stock will stay the same same today")

    

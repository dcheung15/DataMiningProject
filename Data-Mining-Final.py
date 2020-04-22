#Final Project
#Senitiment Analysis

#imports needed
import twitter
from textblob import TextBlob
import datetime

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


company = '$AAL'

#starting time
firstDT = datetime.datetime.now()
print("Start time:",str(firstDT))

#Starting point (company)
company = '$AAL'

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

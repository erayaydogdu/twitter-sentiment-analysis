import tweepy
from textblob import TextBlob
import csv

consumer_key = 'YOUR_CONSUMER_TOKEN'
consumer_secret = 'YOUR_CONSUMER_SECRET'

access_token ='YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

topic = input('Give me twitter topic: ')
public_tweets = api.search(topic)


with open('sentiment_analysis_result.csv', 'w', newline='\n') as  f:
    writer = csv.DictWriter(f,fieldnames=['Tweet','Sentiment'])
    writer.writeheader()
    for tweet in public_tweets:
        text = tweet.text
        #Clean text
        cleanedtext = ' '.join([word for word in text.split(' ') if len(word) > 0 and word[0] != '@' and word[0] == '.' and word[0] != '#' and 'http' not in word and word != 'RT'])
		
        analysis = TextBlob(cleanedtext)

        sentimentStr = analysis.sentiment.polarity
        

        if sentimentStr >= 0:
            polarity = 'Positive'
        else:
            polarity = 'Negative'

        writer.writerow({'Tweet':text, 'Sentiment':polarity})
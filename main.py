import tweepy
from textblob import TextBlob
import csv

consumer_key = 'ur43PXS7FgMvWtX7yQ4BXY7oj'
consumer_secret = 'j4nJlKvejCAIZvIAee2Y77SZgj1C5jcgXyEpP4qmdyfCq39KCj'

access_token ='257074402-NjWt90wfV0Ft7zzsoaFArSH4H5iGfV56OqoS0k1V'
access_token_secret = '4gM3vBobYGy6vjSBeE3MeUXw54Gk0fOyVB8HDmphzSvb5'

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
import sys
import json
import re
import operator
from operator import itemgetter

def build_dict(fn):
    afinnfile = open(fn)
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def extract_tweets(fn):
    tweets_file = open(fn)
    tweets = []
    for tweet in tweets_file:
        json_tweet = json.loads(tweet)
        #if "text" in json_tweet.keys():
            #text = json_tweet["text"].encode('utf-8')
        tweets.append(json_tweet)
    return tweets

def extract_hashtags(tweets):
    hashtags = []
    for tweet in tweets:
        if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:
            for hashtag in tweet["entities"]["hashtags"]:
                unicode_tag = hashtag["text"].encode('utf-8')
                hashtags.append(unicode_tag)

    return hashtags

def top_ten(hashtags):
    frequencies = []
    for hashtag in hashtags:
        tupla = [hashtag, hashtags.count(hashtag)]
        if tupla not in frequencies : frequencies.append(tupla)

    frequencies_sorted = sorted(frequencies, key=itemgetter(1), reverse=True)

    for i in range (0,10):
        print frequencies_sorted[i][0] + " " + str(float(frequencies_sorted[i][1]))

def main():
    tweets = extract_tweets(sys.argv[1])
    hashtags = extract_hashtags(tweets)

    top_ten(hashtags)

if __name__ == '__main__':
    main()
    

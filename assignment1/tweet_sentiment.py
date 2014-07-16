import json
import sys
import re

def hw():
    print 'Hello, world!'

def build_dict(fn):
    afinnfile = open(fn)
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    #print scores.items()
    return scores

def extract_tweets(fn):
    tweets_file = open(fn)
    tweets = []
    for tweet in tweets_file:
        json_tweet = json.loads(tweet)
        if "text" in json_tweet.keys():
            text = json_tweet["text"].encode('utf-8')
            tweets.append(text)
    return tweets

def process_sentiments(tweets, sentiments):
    for tweet in tweets:
        tweet_score = 0
        tweet_words = re.findall(r"[\w']+",tweet)
        for word in tweet_words:
            word_score = sentiments[word.lower()] if word.lower() in sentiments else 0
            tweet_score = tweet_score + word_score
        print float(tweet_score)
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = build_dict(sys.argv[1])
    tweets = extract_tweets(sys.argv[2])
    sentiments = process_sentiments(tweets, scores)

if __name__ == '__main__':
    main()

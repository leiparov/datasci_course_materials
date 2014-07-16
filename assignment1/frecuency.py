import sys
import json

def extract_tweets(fn):
    tweets_file = open(fn)
    tweets = []
    for tweet in tweets_file:
        json_tweet = json.loads(tweet)
        if "text" in json_tweet.keys():
            text = json_tweet["text"].encode('utf-8')
            tweets.append(text)
    return tweets

def extract_terms(words):
    terms_unique = []
    terms_non_unique = words.split()
    for term in terms_non_unique:
        if term not in terms_unique:
            terms_unique.append(term)
    return terms_unique

def calculate_freq(terms, words):
    terms_total = len(words.split())
    for term in terms:
        count = words.count(term)
        frequency = float(count)/float(terms_total)
        print term+" " + str(frequency)
   

def main():
    
    tweets = extract_tweets(sys.argv[1])
    all_terms = ' '.join(tweets)
    terms = extract_terms(all_terms)
    
    calculate_freq(terms, all_terms)

if __name__ == '__main__':
    main()

import sys
import json

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
        if "text" in json_tweet.keys():
            text = json_tweet["text"].encode('utf-8')
            tweets.append(text)
    return tweets

def judge_sentiments(tweets, sentiments):
    tweet_scores = []
    term_sentiments = {}

    for tweet in tweets:
        tweet_score = 0
        tweet_words = tweet.split()

        for word in tweet_words:
            word_score = sentiments[word.lower()] if word.lower() in sentiments else 0
            tweet_score += word_score

            if word not in term_sentiments.keys():
                term_sentiments[word] = word_score

        tweet_scores.append([tweet, tweet_score])

    for term in term_sentiments:
        if term not in sentiments:
            new_score = 0
            num_occurances = 1

            for i in range(0,len(tweet_scores)):
                if term in tweet_scores[i][0]:
                    new_score += tweet_scores[i][1]
                    num_occurances += 1

            new_score /= num_occurances
            term_sentiments[term] = new_score

        print term+" "+str(float(term_sentiments[term]))          

def hw():
    print 'Hello, world!'

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
    judge_sentiments(tweets, scores)

if __name__ == '__main__':
    main()

#- * - coding: utf - 8 -*-
import unicodedata
import string
import re
from nltk.tokenize import RegexpTokenizer
from stemmer import stem
from collections import Counter


def build_voc(list_of_tokens, minimum_df=10):
    words = [num for elem in list_of_tokens for num in elem]
    words = Counter(words)
    print 'Building vocabulary from {0} tokens'.format(len(words.keys()))
    for word in words.keys():
        if words[word] <= minimum_df:
            del words[word]
    print 'Vocabulary composed of {0} tokens'.format(len(words.keys()))
    return words.keys()


def sanitize(token):
    token = token.translate(dict.fromkeys(ord(c) for c in string.punctuation))
    if (token in string.punctuation) or token.isdigit():
        return ""
    return token


def remove_accents(text, method='unicode'):
    if method == 'unicode':
        back =''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))
        return back


def rem_stopwords(get_tweets, stopwords):
    to_be_kept = []
    for i in range(len(get_tweets)):
        intermediate = []
        for j in range(len(get_tweets[i])):
            get_tweets[i][j] = remove_accents(get_tweets[i][j])
            for stop in stopwords:
                if get_tweets[i][j].upper() == stop.strip():
                    get_tweets[i][j] = "deleted"
                    break
            if get_tweets[i][j] != "deleted":
                intermediate.append(stem(get_tweets[i][j].upper())) #there should be stem here.
        to_be_kept.append(intermediate)
    return to_be_kept


def preprocess(get_tweets, stopwords):
    tweets = []
    for tweet in get_tweets:
        tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet) # remove the url from the string
        tokenizer = RegexpTokenizer(r'\w+')
        tokenized = tokenizer.tokenize(tweet)
        intermediate = []
        for token in tokenized:
            token = sanitize(token)
            if (token not in string.ascii_letters) and token != "":
                intermediate.append(token)
        tweets.append(intermediate)
    tweets = rem_stopwords(tweets, stopwords)
    return tweets


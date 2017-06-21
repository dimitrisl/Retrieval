#- * - coding: utf - 8 -*-
import nltk
import unicodedata
import copy
import string
import re
from nltk.tokenize import RegexpTokenizer
from stemmer import stem


def sanitize(token):
    token = token.translate(dict.fromkeys(ord(c) for c in string.punctuation))
    if (token in string.punctuation) or token.isdigit():
        return ""
    return token



def remove_accents(text, method='unicode'):
    text =text
    if method == 'unicode':
        back =''.join(c for c in unicodedata.normalize('NFKD', text)
                       if not unicodedata.combining(c))
        return back


def rem_stopwords(get_tweets, stopwords):
    parallel = copy.deepcopy(get_tweets)
    to_be_kept = []
    for i in range(len(parallel)):
        intermediate = []
        for j in range(len(parallel[i])):
            parallel[i][j] = remove_accents(parallel[i][j])
            for stop in stopwords:
                if parallel[i][j].upper() == stop.strip():
                    parallel[i][j] = "deleted"
                    break
            if parallel[i][j] != "deleted":
                intermediate.append(stem(parallel[i][j].upper()))
                print intermediate[-1]
        to_be_kept.append(intermediate)
    return to_be_kept


def preprocess(get_tweets, stopwords):
    tweets = []
    counter = 0
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


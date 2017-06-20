#- * - coding: utf - 8 -*-
import codecs
from spacy.en import English
import unicodedata
import copy


def remove_accents(text, method='unicode'):
    text =text
    if method == 'unicode':
        back =''.join(c for c in unicodedata.normalize('NFKD', text)
                       if not unicodedata.combining(c))
        return back


def load_files():
    n = codecs.open("NegLex.csv", "r", "utf-8")
    neg_lex = n.readlines()
    n.close()
    p = codecs.open("PosLex.csv", "r", "utf-8")
    pos_lex = p.readlines()
    p.close()
    stop = codecs.open("greekstopwords.txt", "r", "utf-8")
    stopwords = stop.readlines()
    stop.close()
    return neg_lex, pos_lex, stopwords


def load_tweets(filename="tweets.csv"):
    f = codecs.open(filename, "r", 'utf-8')#all the tweets
    fr = f.readline()
    tweets_list = []
    while fr != "":
        if u"****τσίου****" not in fr:
            tweets_list.append(fr)
        fr = f.readline()
    print "We have %s tweets" % len(tweets_list)
    return tweets_list


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
                intermediate.append(get_tweets[i][j])
        to_be_kept.append(intermediate)
    return to_be_kept


def preprocess(get_tweets, stopwords):
    tweets = []
    nlp = English()
    for tweet in get_tweets:
        tokenized = nlp(tweet).sents.next()
        intermediate = []
        for token in tokenized:
            if not (token.is_digit or token.is_punct or token.like_url or token.like_email or token.is_space):
                token = unicode(token)
                intermediate.append(token)
        tweets.append(intermediate)
    tweets = rem_stopwords(tweets, stopwords)
    return tweets


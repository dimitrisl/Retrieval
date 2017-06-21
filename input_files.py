#- * - coding: utf - 8 -*-

import codecs
import os


def load_files():
    n = codecs.open("files%sNegLex.csv" % os.sep, "r", "utf-8")
    neg_lex = n.readlines()
    n.close()
    p = codecs.open("files%sPosLex.csv" % os.sep, "r", "utf-8")
    pos_lex = p.readlines()
    p.close()
    stop = codecs.open("files%sgreekstopwords.txt" % os.sep, "r", "utf-8")
    stopwords = stop.readlines()
    stop.close()
    return neg_lex, pos_lex, stopwords


def load_tweets(filename="files%stweets.csv" % os.sep):
    f = codecs.open(filename, "r", 'utf-8')#all the tweets
    fr = f.readline()
    tweets_list = []
    while fr != "":
        if u"****τσίου****" not in fr:
            tweets_list.append(fr)
        fr = f.readline()
    print "We have %s tweets" % len(tweets_list)
    return tweets_list

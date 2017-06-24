#- * - coding: utf - 8 -*-
import codecs
import os


def get_the_stem(em_lexicon):
    back = []
    for line in em_lexicon:
        back.append(line.split(",")[-1])
    return back


def read_n_list(file_object):
    lista = []
    line = file_object.readline().strip()
    while line != "":
        lista.append(line)
        line = file_object.readline().strip()
    return lista


def load_files():
    n = codecs.open("files%sNegLex.csv" % os.sep, "r", "utf-8")
    neg_lex = read_n_list(n)
    n.close()
    p = codecs.open("files%sPosLex.csv" % os.sep, "r", "utf-8")
    pos_lex = read_n_list(p)
    p.close()
    stop = codecs.open("files%sgreekstopwords.txt" % os.sep, "r", "utf-8")
    stopwords = stop.readlines()

    stop.close()
    return neg_lex[1:], pos_lex[1:], stopwords


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

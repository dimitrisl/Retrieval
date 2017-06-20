import codecs


def load_files():
    n = codecs.open("NegLex.csv", "r", "utf-8")
    neg_lex = n.readlines()
    n.close()
    p = codecs.open("PosLex.csv", "r", "utf-8")
    pos_lex = n.readlines()
    p.close()
    stop = codecs.open("GrStemmer.txt", "r", "utf-8")
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


def preprocess(tweets):
    pass


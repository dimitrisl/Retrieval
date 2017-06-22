# -*- coding: cp1253 -*-
from input_files import load_tweets
from input_files import load_files
from preprocessor import preprocess
from preprocessor import build_voc
import time

start = time.time()

neg_lex, pos_lex, stopwords = load_files()
stemmed_vocabulary = build_voc(neg_lex, pos_lex)

get_tweets = load_tweets() # it takes the filename as an argument
#sanitize tweets
print get_tweets[1]
tweets = preprocess(get_tweets, stopwords)

for line in tweets[1]:
    print line

print time.time() - start

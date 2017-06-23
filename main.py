# -*- coding: cp1253 -*-
from input_files import load_tweets
from input_files import load_files
from preprocessor import preprocess
from preprocessor import build_voc
from tools import *
import time

start = time.time()

neg_lex, pos_lex, stopwords = load_files()

get_tweets = load_tweets() # it takes the filename as an argument
# sanitize tweets
print get_tweets[1]
tweets = preprocess(get_tweets, stopwords)

# build vocabulary from preprocessed tweets
vocabulary = build_voc(tweets)


X = termTweet(vocabulary,tweets)  # calculate Term-tweets Matrix(mxn)
C = corrMatrix(X)  # calculate corrMatrix(mxm)
PMI = ppmi(C)  # calculate PPMI matrix
print 'Matrix PMI is of shape: ', PMI.shape

#U, S, V = svdcal(PPMI)

#after normalizing it
#we have to check if i,j word belong to a negative or a positive cluster (knn)
#i assume it's the pmi

#print 'Matrix PPMI is of shape: ', U.shape
for line in tweets[1]:
    print line

print time.time() - start

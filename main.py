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


X = termTweet(vocabulary, tweets)  # calculate Term-tweets Matrix(mxn)
C = corrMatrix(X)  # calculate corrMatrix(mxm)
PPMI = ppmi(C)  # calculate PPMI matrix
print 'Matrix PPMI is of shape: ', PPMI.shape

# Calculate SVD matrices
U, S, V = svdcal(PPMI)

print 'Matrix U is of shape: ', U.shape

# normalize with euclidean norm the matrix U of the vector embeddings
Uk = normalizematrix(U)

print time.time() - start

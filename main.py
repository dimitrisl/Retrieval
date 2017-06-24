# -*- coding: cp1253 -*-
from input_files import load_tweets
from input_files import load_files
from preprocessor import preprocess
from preprocessor import build_voc
from tools import *
from input_files import get_the_stem
import time

start = time.time()

neg_lex, pos_lex, stopwords = load_files()

stem_pos_lex = get_the_stem(pos_lex)# get the stemmed version of the word
stem_neg_lex = get_the_stem(neg_lex)

get_tweets = load_tweets() # it takes the filename as an argument
# sanitize tweets
tweets = preprocess(get_tweets, stopwords)
print "pre-processing done"

vocabulary = build_voc(tweets, 80) # we use a very small vocabulary on purpose.

X = termTweet(vocabulary, tweets)  # calculate Term-tweets Matrix(mxn)
C = corrMatrix(X)  # calculate corrMatrix(mxm)
PPMI = ppmi(C)  # calculate PPMI matrix
print 'Matrix PPMI is of shape: ', PPMI.shape

# Calculate SVD matrices
U, S, V = svdcal(PPMI)

print 'Matrix U is of shape: ', U.shape

# normalize with euclidean norm the matrix U of the vector embeddings
Uk = normalizematrix(U)
#start knn
lex_pos, lex_ne = knn(Uk, vocabulary, stem_pos_lex, stem_neg_lex, 3)

print "positive | negative"
print len(lex_pos.keys()), len(lex_ne.keys())
print time.time() - start

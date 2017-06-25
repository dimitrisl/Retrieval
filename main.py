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

vocabulary = build_voc(tweets,50) # we use a very small vocabulary on purpose.

X = termTweet(vocabulary, tweets)  # calculate Term-tweets Matrix(mxn)
C = corrMatrix(X)  # calculate corrMatrix(mxm)
PPMI = ppmi(C)  # calculate PPMI matrix
print 'Matrix PPMI is of shape: ', PPMI.shape

# Calculate SVD matrices
U, S, V = svdcal(PPMI)

print 'Matrix U is of shape: ', U.shape

embedding_type = raw_input('Choose type of embedding matrix E(state the number):1)Ε=Uk 2) E=Uk.T*Sk 3) E=Uk.T*Sk^1/2: ')
if embedding_type == 1:
    E = normalizematrix(U)
elif embedding_type == 2:
    E = U.T.dot(S)
    E = normalizematrix(E)
elif embedding_type == 3:
    E = U.T.dot(np.sqrt(S))
    E = normalizematrix(E)


#start knn
lex_pos, lex_ne = knn(E, vocabulary, stem_pos_lex, stem_neg_lex, 3)

print "positive | negative"
print len(lex_pos.keys()), len(lex_ne.keys())
print time.time() - start

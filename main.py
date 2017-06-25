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
# it takes the filename as an argument
get_tweets = load_tweets()
# sanitize tweets
tweets = preprocess(get_tweets, stopwords)
print "pre-processing done"

vocabulary = build_voc(tweets, 10)

X = termTweet(vocabulary, tweets)  # calculate Term-tweets Matrix(mxn)
C = corrMatrix(X)  # calculate corrMatrix(mxm)
PPMI = ppmi(C)  # calculate PPMI matrix
print 'Matrix PPMI is of shape: ', PPMI.shape

# Calculate SVD matrices
U, S, V = svdcal(PPMI, 300)

print 'Matrix U is of shape: ', U.shape

embedding_type = input('Choose type of embedding matrix E(state the number):1)Ε=Uk 2) E=Uk.T*Sk 3) E=Uk.T*Sk^1/2: ')
if embedding_type == 1:
    E = normalizematrix(U)
elif embedding_type == 2:
    E = U.dot(S)
    E = normalizematrix(E)
elif embedding_type == 3:
    E = U.T.dot(np.sqrt(S))
    E = normalizematrix(E)


#start knn
lex_pos, lex_ne = knn(E, vocabulary, stem_pos_lex, stem_neg_lex, 3)

print "positive | negative"
print len(lex_pos.keys()), len(lex_ne.keys())

lex_ne, neg_counter, new_neg = not_in_lex(lex_ne, stem_neg_lex, vocabulary)
print "%s negative words don't belong in the negative lexicon" % neg_counter
lex_pos, pos_counter, new_pos = not_in_lex(lex_pos, stem_pos_lex, vocabulary)
print "%s positive words don't belong in the positive lexicon" % pos_counter
write_file(lex_ne, "Neg") # write the words to ExNeg
write_file(lex_pos, "Pos")
##################################################
new = dict()
new["newNeg.txt"] = new_neg
new["newPos.txt"] = new_pos
write_file(new, "New", "new")

print time.time() - start

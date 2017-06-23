# -*- coding: cp1253 -*-
from input_files import load_tweets
from input_files import load_files
from preprocessor import preprocess
from preprocessor import build_voc
import time

start = time.time()

neg_lex, pos_lex, stopwords = load_files()

get_tweets = load_tweets() # it takes the filename as an argument
#sanitize tweets
print get_tweets[1]
tweets = preprocess(get_tweets, stopwords)
vocabulary = build_voc(tweets, 15) # How will we determine the size of the vocabulary?
# apply the pmi here?

# We have to find the embeddings matrix!
#after normalizing it
#we have to check if i,j word belong to a negative or a positive cluster (knn)
#i assume it's the pmi


for line in tweets[1]:
    print line

print time.time() - start

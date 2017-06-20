#- * - coding: utf - 8 -*-
from preprocessor import load_tweets
from preprocessor import load_files
from preprocessor import preprocess


neg_lex, pos_lex, stopwords = load_files()
print neg_lex[1],pos_lex[1], stopwords[1]
get_tweets = load_tweets() # it takes the filename as an argument
#sanitize tweets
tweets = preprocess(get_tweets, stopwords)
print tweets[2]
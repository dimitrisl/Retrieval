#- * - coding: utf - 8 -*-
from preprocessor import load_tweets
from preprocessor import load_files
from preprocessor import preprocess


neg_lex, pos_lex, stopwords = load_files()
get_tweets = load_tweets() # it takes the filename as an argument
#sanitize tweets
print get_tweets[1]
tweets = preprocess(get_tweets, stopwords)
tweets = tweets
print tweets[1], type(tweets[1][1])

for line in tweets[1]:
    print line
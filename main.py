#- * - coding: utf - 8 -*-
from preprocessor import load_tweets
from preprocessor import load_files


neg_lex, pos_lex, stopwords = load_files()
tweets = load_tweets() # it takes the filename as an argument
# we will probably call preprocessing in load tweets def in order to have the pure information
#from them in the main function
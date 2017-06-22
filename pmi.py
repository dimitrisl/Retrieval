import numpy as np


def termTweet(words, tweets):
    intermediate = [[]]
    for i in words:
        for j in tweets:
            if i in j:
                intermediate[i][j] = 1
            else:
                intermediate[i][j] = 1
    X = np.array(intermediate)
    return X


def corrMatrix(X):
    return X.dot(X.T)


def pmi(C):
    Ci = np.sum(C, axis=1)
    Cj = np.sum(C, axis=0)
    N = np.sum(C)
    CiCj = Ci*Cj
    PMI = np.log(np.divide(N*C, CiCj))
    return PMI

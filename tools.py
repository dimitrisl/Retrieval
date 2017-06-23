import numpy as np
from scipy import linalg


def termTweet(words, tweets):
    X = np.zeros((len(words), len(tweets)))
    for wi, i in enumerate(words):
        for wj, j in enumerate(tweets):
            if i in j:
                X[wi, wj] = 1
    return X

def corrMatrix(X):
    return X.dot(X.T)


def ppmi(C):
    Ci = np.sum(C, axis=1)
    Cj = np.sum(C, axis=0)
    N = np.sum(Ci)
    CiCj = Ci.dot(Cj)
    PPMI = np.zeros((C.shape[0], C.shape[1]))

    for i in range(0, C.shape[0]):
        for j in range(0, C.shape[1]):
            if C[i, j] == 0:
                PPMI[i, j] = 0
            else:
                PPMI[i, j] = np.log(np.divide(N * C, CiCj))
    return PPMI

def svdcal(a):
    U, S, V = linalg.svd(a)
    return U, S, V
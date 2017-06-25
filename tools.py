from __future__ import division
import numpy as np
from scipy import linalg
from math import log


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
    #CiCj = Ci.dot(Cj)
    PPMI = np.zeros((C.shape[0], C.shape[1]))

    for i in range(0, C.shape[0]):
        for j in range(0, C.shape[1]):
            if C[i, j] == 0:
                PPMI[i, j] = 0
            else:
                PPMI[i, j] = log(N * C[i, j]/Ci[i]*Cj[j])
    return PPMI


def svdcal(a):
    U, S, V = linalg.svd(a)
    return U, S, V


def normalizematrix(A):
    norm_vector = linalg.norm(A, axis=1)
    normalized_matrix = np.divide(A, norm_vector)
    return normalized_matrix


def get_top_k_distances(U, counter, to_be_visited, K):
    distances = []
    for index in to_be_visited:
        diff = linalg.norm((U[counter] - U[index]))
        distances.append((diff, index))

    distances.sort()
    indexes = [counter]
    for x, y in distances[:K]:
        indexes.append(y)
        to_be_visited.remove(y)
    return indexes


def knn(U, voc, stem_pos_lex, stem_neg_lex, K):

    to_be_visited = [i for i in range(U.shape[0])]
    pos_lex = dict()
    neg_lex = dict()
    poped = []
    while to_be_visited:
        if voc[to_be_visited[0]] in stem_pos_lex:
            temp = to_be_visited[0]
            pos_lex[temp] = []
            indexes = get_top_k_distances(U, to_be_visited[0], to_be_visited + poped, K)
            to_be_visited = list(set(to_be_visited) - set(indexes)) # remove all the indexes that are clustered to the positive from now on.
            pos_lex[temp].extend(indexes) # fill this field with all the indexes of the lines we need
            del to_be_visited[0]
        elif voc[to_be_visited[0]] in stem_neg_lex:
            temp = to_be_visited[0]
            neg_lex[temp] = []
            indexes = get_top_k_distances(U, to_be_visited[0], to_be_visited + poped, K)
            to_be_visited = list(set(to_be_visited) - set(indexes))
            neg_lex[temp].extend(indexes)
            del to_be_visited[0]
        else:
            poped.append(to_be_visited[0])
            del to_be_visited[0]
        print len(to_be_visited)
    return pos_lex, neg_lex

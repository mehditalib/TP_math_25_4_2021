# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:16:44 2021

@author: Hatim NAQOS
"""

import numpy as np

def dimensions(A):
    if A:
        return len(A),len(A[0])

def affiche(A):
    for ligne in A:
        print(ligne)

def matriceNulle(n,p):
    return [[0 for j in range(p)]for i in range(n)]


def matriceUnite(n):
    A = matriceNulle(n,n)
    for i in range(len(A)):
        A[i][i] = 1
    return A


def transpose(A):
    d = dimensions(A) 
    return [[A[j][i]for j in range(d[0])]for i in range(d[1])]


def estTriangulaireSup(A):
    n,p = dimensions(A)
    assert n == p
    for i in range(len(A)):
        for j in range(i):
            if A[i][j] != 0:
                return False
    return True

           
def sommeMatrice(A,B):
    n,p = dimensions(A)
    q,r = dimensions(B)
    assert (n,p) == (q,r)
    return [[A[i][j]+B[i][j] for j in range(p)]for i in range(n)]


def multScalaire(A,n):
    m,p = dimensions(A)
    return [[n * A[i][j] for j in range(m)]for i in range(p)]


def produitMatrice(A,B):
    n,p = dimensions(A)
    q,r = dimensions(B)
    assert p == q
    C = matriceNulle(n,r)
    for i in range(n):
        for j in range(q):
            for k in range(p):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


def blocs(A,a,b):
    n = dimensions(A)[0]
    C = matriceNulle(n*a,b*n)
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = A[i%n][j%n]   
    return C                 


def exponaif(A,n):
    if n == 0:
        return matriceUnite(dimensions(A)[0])
    else: 
        C = A
        for i in range(1,n):
            C = produitMatrice(C,A)
        return C

A = [[0,1],[1,1]]
affiche(exponaif(A,45))



        
        
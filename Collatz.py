#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

import sys
import select

from datetime import datetime

d = {1:1}

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    v1 = 0
    v2 = 0
    a = s.split()
    try: 
        v1 = int(a[0])
        v2 = int(a[1])
    except:
        return ""
    #if(int(a[0])<0 || int(a[1])<0):
    #assert False 
    return [v1, v2]

# ------------
# cycle_length
# ------------

def cycle_length (n) :
    k = n
    c = 0
    if n in d:
        return d[n]
    elif(n>1):
        if (n % 2) == 0 :
            n = (n // 2)
            c = cycle_length(n)
        else :
            n = (3 * n) + 1
            c = cycle_length(n)
    c+=1
    d[k] = c
    return c

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """


    intMax = 0
    x = 0

    if (j<i):
        y = i
        i = j
        j = y

    for y in range(i,j+1):
        x = cycle_length(y)
        if (x> intMax):
            intMax = x

    return intMax

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if(len(s)>=2):
            i, j = collatz_read(s)
            v = collatz_eval(i, j)
            collatz_print(w, i, j, v)




#!/usr/bin/python3

import os, re
cou = 0

with open("input3") as f:
    for line in f:
        strs = line.split()
        mini = int(strs[0])
        maxi = int(strs[1])
        char = strs[2]
        pasw = strs[3]
        howmany = pasw.count(char)

        if howmany >= mini and howmany <= maxi:
            cou = cou + 1

print ( cou )

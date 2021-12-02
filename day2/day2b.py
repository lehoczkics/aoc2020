#!/usr/bin/python3

import os, re
cou = 0

def splitter(word):
    return [char for char in word]

with open("input3") as f:
    for line in f:
        strs = line.split()
        pos1 = int(strs[0])
        pos2 = int(strs[1])
        char = strs[2]
        pasw = strs[3]
        paswch = splitter(pasw)

        hit1 = 0
        hit2 = 0
        if paswch[pos1-1] == char :
            hit1 = 1
        if paswch[pos2-1] == char:
            hit2 = 1

        if hit1 + hit2 == 1:
            cou = cou + 1

print ( cou )

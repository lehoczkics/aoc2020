#!/usr/bin/env python3

import os, re
cou = 0
right = 0
lineno = 1

def splitter(word):
    return [char for char in word]

with open("input.txt") as f:
    for line in f:
        strs = splitter(line)
        rpos = right % 31
        # print("Line: ", lineno, " column: ", rpos, " char: ", strs[rpos])
        if strs[rpos] == "#" :
            cou = cou + 1
        right = right + 1
        lineno = lineno + 1

print(cou)


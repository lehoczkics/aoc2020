#!/usr/bin/env python3

import os, re
rshift = [1,3,5,7,1]
dshift = [1,1,1,1,2]

def splitter(word):
    return [char for char in word]

for i in range(len(rshift)) :
    cou = 0
    right = 0
    lineno = 0
    with open("input.txt") as f:
        for line in f:
            if lineno % dshift[i] == 1:
                lineno = lineno + 1
                continue
            strs = splitter(line)
            rpos = right % 31
            # print("Line: ", lineno, " column: ", rpos, " char: ", strs[rpos])
            if strs[rpos] == "#" :
                cou = cou + 1
            right = right + rshift[i]
            lineno = lineno + 1

    print(cou)

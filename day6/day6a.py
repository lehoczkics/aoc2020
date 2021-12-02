#!/usr/bin/env python3

import os
howmany = 0
yesletters = []

def splitter(word):
    return [char for char in word]

with open("input.txt") as f:
    for line in f:
        if line == '\n':
            print(yesletters)
            howmany = howmany + len(yesletters)
            yesletters = []
        else :
            mychars = splitter(line)
            for x in mychars :
                if x == '\n' :
                    continue
                elif x not in yesletters :
                    yesletters.append(x)

print(howmany)

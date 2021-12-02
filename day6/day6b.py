#!/usr/bin/env python3

import os, string

letterdict = {}
answers = 0
howmany = 0

def splitter(word):
    return [char for char in word]

def allzero():
    for mych in splitter(string.ascii_lowercase):
        letterdict[mych] = 0

allzero()

with open("input.txt") as f:
    for line in f:
        if line == '\n':
            for x in letterdict.values():
                if x == answers :
                    howmany = howmany + 1
            # print(answers, " answers given")
            # print(letterdict)
            answers = 0
            allzero()
        else :
            mychars = splitter(line)
            for x in mychars :
                if x == '\n' :
                    answers = answers + 1
                    continue
                else :
                    y = letterdict[x]
                    letterdict[x] = y + 1

print(howmany)

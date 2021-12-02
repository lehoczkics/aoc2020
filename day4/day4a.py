#!/usr/bin/env python3

import os

howmany = 0
allpassports = 0
eightfields = 0
allseven = 0
sevenfields = 0

fields = []
musthave = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }

with open("input2") as f:
   for line in f:
        if line in ['\n']:
            allpassports = allpassports + 1
            if len(fields) == 8:
                eightfields = eightfields +1
            if len(fields) == 7:
                allseven = allseven + 1
                if not "cid" in fields:
                    sevenfields = sevenfields + 1

#            print(fields)
            myset = set(fields)
            if musthave.issubset(myset) :
                howmany = howmany + 1
            fields = []
        else:
           fields.append(line.rstrip())


print("eight: ", eightfields)
print("seven: ", allseven)
print("seven and valid: ", sevenfields)
print("valid: ", howmany)
print("all: ", allpassports)
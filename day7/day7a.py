#!/usr/bin/python

import os, re

def bagcontains(bag):
    # returns a list of bags which can contain the current bag
    baglist = []
    with open("input.txt") as f:
        for line in f:
            if re.search('.*\d+\s%s.*' %bag,line):
                mybag = re.search('^(\w+\s+\w+)', line).group(1)
#                print(mybag)
                baglist.append(mybag)
    
    return baglist

found = []
notyetsearched = []
puffer = ["shiny gold"]

while puffer:
    for item in puffer:
        baginbag = bagcontains(item)
        notyetsearched.extend(baginbag)
        # print("Notyetsearched: ", notyetsearched)

    found.extend(notyetsearched)
    puffer = []
    puffer.extend(notyetsearched)
    notyetsearched = []
    # print("Puffer: ", puffer)

print(found)
print(len(found))

foundset = set(found)
print(len(foundset))

#!/usr/bin/ebv pyhton3

import os

mymax = 0

allseats = []

for i in range(0,923) :
    allseats.append(i)

#print(allseats)

def btd(n):
    return int(n,2)

with open("input1") as f:
    for line in f:
        myseat = btd(line)
        print(myseat)
        allseats.remove(myseat)
#        print(line)
#        rowstr = line[0:7]
#        colstr = line[7:11]
#        print(rowstr, "-", colstr)
#        print(btd(rowstr), "-", btd(colstr))
#        seatid = 8*btd(rowstr) + btd(colstr)
#        if seatid > mymax :
#            mymax = seatid

print("unallocated: ", allseats)
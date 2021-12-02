#!/usr/bin/env python3

def valide (list, num):
    for i in range(0,len(list)):
        for j in range(i,len(list)):
            if num == list[i] + list[j]:
                return(True)
    return(False)

my25 = []

with open("input.txt") as f:
    for line in f:
        newnum = int(line)
        if len(my25) < 25 :
            my25.append(newnum)
        else :
            if valide(my25, newnum):
                # number found as addition
                del my25[0]
                my25.append(newnum)
                continue
            else:
                print(newnum)
                break


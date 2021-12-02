#!/usr/bin/env python3

magicno = 22477624
numlist = []
with open("input.txt") as f:
    for line in f:
        if int(line) == magicno :
            break
        else :
            numlist.append(int(line))

for i in range(0,len(numlist)):
    mysum = numlist[i]
    for j in range(i+1,len(numlist)):
        mysum += numlist[j]
        # print(mysum)
        if mysum == magicno:
            print("gotcha! ", i, " ", j)
            contig = []
            for k in range(i,j):
                contig.append(numlist[k])
            
            print( min(contig) + max(contig) )

        elif mysum > magicno:
            # print("too big")
            break


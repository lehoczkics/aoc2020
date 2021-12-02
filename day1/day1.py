#!/usr/bin/env python3

import os

with open("input.txt") as f:
    content = f.readlines()

print("There are ", len(content), " numbers in input." )

for i in range(0,len(content)):
    for j in range(i-1,len(content)):
        sum = int(content[i]) + int(content[j])
        if sum == 2020:
            product = int(content[i]) * int(content[j])
            print(content[i], " and ", content[j], " szorozva ", product)
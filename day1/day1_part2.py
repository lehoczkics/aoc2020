#!/usr/bin/env python3

import os

with open("input.txt") as f:
    texts = f.readlines()

nums = [int(x) for x in texts]
leng=len(nums)

print("There are ", leng, " numbers in input." )

for i in range(0,leng):
    for j in range(i-1,leng):
        for k in range(j-1,leng):
            sum = nums[i] + nums[j] + nums[k]
            if sum == 2020:
                product = nums[i] * nums[j] * nums[k]
                print(nums[i], " and ", nums[j], " and ",nums[k], " szorozva ", product)
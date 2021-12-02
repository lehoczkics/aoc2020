#!/usr/bin/env python3

onejolt = 0
threejolt = 0
whatjolt = 0

with open("sorted") as f:
    for line in f:
        if int(line) - whatjolt == 1 :
            onejolt += 1
        elif int(line) - whatjolt == 3 :
            threejolt += 1
        whatjolt = int(line)

print(onejolt * threejolt)

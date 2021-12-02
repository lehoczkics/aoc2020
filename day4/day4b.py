#!/usr/bin/env python3

import os, re

howmany = 0
valid = []
musthave = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }

with open("input1") as f:
   for line in f:
        if line in ['\n']:
            # end of passport, go check
            print(valid)
            myset = set(valid)
            if musthave.issubset(myset) :
                howmany = howmany + 1
            valid = []
        else:
            # next password pattern
            if line[0:3] == 'byr':
                mybyr = re.search('^byr:(\d{4})$',line).group(1)
                if int(mybyr) >= 1920 and int(mybyr) <= 2020 :
                    valid.append("byr")
                    print(mybyr)

            elif line[0:3] == 'iyr':
                myiyr = re.search('^iyr:(\d{4})$',line).group(1)
                if int(myiyr) >= 2010 and int(myiyr) <= 2020 :
                    valid.append("iyr")
                    print(myiyr)

            elif line[0:3] == 'eyr':
                myeyr = re.search('^eyr:(\d{4})$',line).group(1)
                if int(myeyr) >= 2020 and int(myeyr) <= 2030 :
                    valid.append("eyr")
                    print(myeyr)

            elif line[0:3] == 'hgt' :
                matchcm = re.search('^hgt:([0-9]+)cm$',line)
                matchin = re.search('^hgt:([0-9]+)in$',line)
                if matchcm:
                    mycm = re.search('^hgt:([0-9]+)cm$',line).group(1)
                    print(mycm, "cm")
                    if int(mycm) >= 150 and int(mycm) <= 193 :
                        valid.append("hgt")
                elif matchin :
                    myin = re.search('^hgt:([0-9]+)in$',line).group(1)
                    print(myin, "in")
                    if int(myin) >= 59 and int(myin) <= 76 :
                        valid.append("hgt")

            elif line[0:3] == 'hcl' :
                if re.search('^hcl:#[0-9a-f]{6}$',line) :
                    valid.append("hcl")
                    print("hcl")

            elif line[0:3] == 'ecl':
                if line[4:7] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid.append("ecl")
                    print("ecl ", line[4:7])
            
            elif line[0:3] == 'pid':
                if re.search('^pid:[0-9]{9}$',line) :
                    valid.append("pid")
                    print("pid")

print("VALID: ", howmany)
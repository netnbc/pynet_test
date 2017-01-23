#!/usr/bin/env python

#### READ ####
f = open("labreadfile1_01232017.txt")
for line in f:
    print line.strip()

f.seek(0)
file_data = f.readlines()
for line in file_data:
    print line.strip()

f.seek(0)
file_data = f.read()
for line in file_data.splitlines():
    print line

f.close()

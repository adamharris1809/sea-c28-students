#!/usr/bin/env python

import io

try:
    f = io.open('/home/adamharris/sea-c28-stuff/sea-c28-students/Students/AdamHarris/session04/sherlock.txt')
except:
    print("this didn't work")

while True:
    line = f.readline()
    if not line:
        break

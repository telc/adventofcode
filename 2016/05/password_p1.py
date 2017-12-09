#!/usr/bin/env python

from hashlib import md5

input = 'wtnhxymk'
doorid = 0
pw = ''
while(len(pw) < 8):
  hash = md5(input + str(doorid)).hexdigest()
  if hash[:5] == '00000':
    pw += hash[5]
  doorid += 1
print pw

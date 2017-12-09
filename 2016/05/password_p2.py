#!/usr/bin/env python

from hashlib import md5

input = 'wtnhxymk'
doorid = 0
pw = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
count = 0
while(count < 8):
  hash = md5(input + str(doorid)).hexdigest()
  if hash[:5] == '00000':
    if ord('0') <= ord(hash[5]) and ord(hash[5]) <= ord('7'):
      if pw[int(hash[5])] == ' ':
        pw[int(hash[5])] = hash[6]
        count += 1
        print ''.join(pw)
  doorid += 1
print ''.join(pw)

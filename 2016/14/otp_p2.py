#!/usr/bin/env python

from hashlib import md5
import re

salt = 'ihaygndm'
#salt = 'abc'
possible = {}
keys = set()
lastIdx = 0

i = 0
triple = re.compile(r'(.)\1\1')
while len(keys) < 64:
  key = md5(salt + str(i)).hexdigest()
  for _ in range(2016):
    key = md5(key).hexdigest()

  for idx in sorted(possible.keys()):
    p = possible[idx]
    if key.find(p['char']*5) != -1:
      keys.add(p['key'])
#      print len(keys), i, idx
      if idx > lastIdx:
        lastIdx = idx
      del possible[idx]
  if i - 1000 in possible:
    del possible[i-1000]
  match = triple.search(key)
  if match:
    possible[i] = {'key': key, 'char': match.group(1)}
  i += 1
print lastIdx

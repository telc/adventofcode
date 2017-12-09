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
  done = []
  for p in possible.values():
    if key.find(p['char']*5) != -1:
      keys.add(p['key'])
      if p['idx'] > lastIdx:
        lastIdx = p['idx']
      done.append(p['idx'])
  for d in done:
    del possible[d]
  if i - 1000 in possible:
    del possible[i-1000]
  match = triple.search(key)
  if match:
    possible[i] = {'key': key, 'char': match.group(1), 'idx': i}
  i += 1
print lastIdx

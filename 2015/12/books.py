#!/usr/bin/env python

import json

s = 0

def parseList(l):
  global s
  for value in l:
    if type(value) == list:
      parseList(value)
    elif type(value) == dict:
      parseDict(value)
    elif type(value) == int:
      s += value

def parseDict(d):
  global s
  if 'red' in d.values():
    return
  for key, value in d.iteritems():
    if type(value) == dict:
      parseDict(value)
    elif type(value) == list:
      parseList(value)
    elif type(value) == int:
      s += value

if __name__ == '__main__':
  with open('input', 'r') as f:
    data = json.loads(f.read())

  parseDict(data)
  print s

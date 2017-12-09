#!/usr/bin/env python

def encodedLen(string):
  l = -2
  xr = iter(xrange(len(string)))
  for i in xr:
    l += 1
    if string[i] == '\\':
      next(xr)
      if string[i+1] == 'x':
        next(xr)
        next(xr)
  return l

def stringDiff(string):
  return len(string) - encodedLen(string)

def reencodedLen(string):
  l = 2
  for s in string:
    l += 1
    if s == '"':
      l += 1
    if s == '\\':
      l += 1
  return l

def newStringDiff(string):
  return reencodedLen(string) - len(string)

if __name__ == '__main__':
  with open('input', 'r') as f:
    strings = f.read().splitlines()

  s = 0
  t = 0
  for string in strings:
    s += stringDiff(string)
    t += newStringDiff(string)

  print s, t

#!/usr/bin/env python

import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def numVowels(string):
  count = 0
  for s in string:
    if s in vowels:
      count += 1
  return count

def isIllegal(pair):
  if pair == 'ab':
    return True
  if pair == 'cd':
    return True
  if pair == 'pq':
    return True
  if pair == 'xy':
    return True
  return False

def isNice(string):
  has_double = False
  for i in range(len(string)-1):
    pair = string[i:i+2]
    if pair[0] == pair[1]:
      has_double = True
    if isIllegal(pair):
      return False
  return numVowels(string) >= 3 and has_double

def isReallyNice(string):
  has_double = False
  has_repeating = False
  for i in range(len(string)-1):
    tripple = string[i:i+3]
    pair = string[i:i+2]
    if len(tripple) == 3 and tripple[0] == tripple[2]:
      has_repeating = True
    for j in range(i+2, len(string)-1):
      pair2 = string[j:j+2]
      if pair == pair2:
        has_double = True
  return has_double and has_repeating

if __name__ == '__main__':
  with open('input', 'r') as f:
    strings = f.read().splitlines()

  nice1 = 0
  nice2 = 0
  for string in strings:
    if isNice(string):
      nice1 += 1
    if isReallyNice(string):
      nice2 += 1
  print nice1, nice2

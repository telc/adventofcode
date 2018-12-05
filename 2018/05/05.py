#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = f.read().strip()

#input_ = "dabAcCaCBAcCcaDA"

def part1(input_):
  i = 0
  while i < len(input_) - 1:
    if abs(ord(input_[i]) - ord(input_[i+1])) == 0x20:
      input_ = input_[:i] + input_[i+2:]
      i -= 1
    else:
      i += 1
  return len(input_)

def part2(input_):
  return 0

if __name__ == '__main__':
  print part1(input_), part2(input_)

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
      if i < 0:
        i = 0
    else:
      i += 1
  return len(input_)

def part2(input_):
  best_len = 99999999
  for c in xrange(ord('a'), ord('z')+1):
    tmp = input_.replace(chr(c), '')
    tmp = tmp.replace(chr(c-0x20), '')
    tmp_len = part1(tmp)
    if tmp_len < best_len:
      best_len = tmp_len
  return best_len

if __name__ == '__main__':
  print part1(input_), part2(input_)

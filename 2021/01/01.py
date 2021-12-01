#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()]

with open('test', 'r') as f:
  test_ = [int(x) for x in f.read().splitlines()]


def p1(depths):
  prev = 0
  count = 0
  for i in depths:
    if prev:
      if i > prev:
        count += 1
    prev = i
  return count

def p2(depths):
  window = []
  count = 0
  for i in depths:
    window.append(i)
    if len(window) == 4:
      if sum(window[:3]) < sum(window[1:]):
        count += 1
      window.pop(0)
  return count

if __name__ == '__main__':
  print p1(input_)
  print p2(input_)

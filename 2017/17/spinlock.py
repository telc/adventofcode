#!/usr/bin/env python2.7

steps = 324
test = 3

def spinlock(steps, spins):
  pos = 0
  buf = [0]
  for i in xrange(1,spins+1):
    pos = (pos + steps) % i + 1
    buf.insert(pos,i)
  return buf

def part2(steps):
  pos = 0
  value = 0
  for i in xrange(1,50000000+1):
    pos = (pos + steps) % i + 1
    # 0 is always first, so only save value in pos 1
    if pos == 1:
      value = i
  return value

if __name__ == '__main__':
  buf = spinlock(steps, 2017)
  p = buf.index(2017) + 1
  print buf[p%len(buf)]

  print part2(steps)

#!/usr/bin/env python

lengths = "18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"

nums = []
pos = 0
skip = 0

def solve(lengths):
  global nums
  global pos
  global skip

  for length in lengths:
    nums = nums[length:] + nums[0:length][::-1]
    nums = nums[skip%len(nums):] + nums[0:skip%len(nums)]
    pos = (pos + length + skip) % len(nums)
    skip += 1
  return nums[-pos:] + nums[:-pos]

def init():
  global nums
  global pos
  global skip

  nums = [i for i in range(256)]
  pos = 0
  skip = 0

def part1(lengths):
  init()
  lengths = map(int,lengths.split(','))

  h = solve(lengths)
  return h[0] * h[1]

def part2(lengths):
  init()
  lengths = map(ord,lengths) + [17, 31, 73, 47, 23]
  
  sparse = []
  for i in range(64):
    sparse = solve(lengths)

  dense = []
  p = 0
  for i in range(16):
    dense.append( reduce((lambda a, b: a ^ b), sparse[p:p+16]) )
    p += 16

  return ''.join(map('{0:02x}'.format, dense))

print part1(lengths)
print part2(lengths)

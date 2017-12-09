#!/usr/bin/env python

import sys

def calculate_paper(l, w, h):
  lw = l*w
  wh = w*h
  hl = h*l

  mini = sys.maxint
  if (lw < mini):
    mini = lw
  if (wh < mini):
    mini = wh
  if (hl < mini):
    mini = hl

  return 2*lw + 2*wh + 2*hl + mini

def calculate_ribbon(l, w, h):
  dim = [l, w, h]
  dim.sort()
  return reduce(lambda x, y: x*2+y*2, dim[:-1]) + l*w*h

if __name__ == '__main__':
  with open('input', 'r') as f:
    dims = f.read().splitlines()

  paper = 0
  ribbon = 0
  for dim in dims:
    d = map(int, dim.split('x'))
    paper += calculate_paper(*d)
    ribbon += calculate_ribbon(*d)

  print paper, ribbon

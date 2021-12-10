#!/usr/bin/env python3
from statistics import median

def solve(lines):
  openers = ['(', '[', '{', '<']
  closers = [')', ']', '}', '>']
  ovalues = [1, 2, 3, 4]
  cvalues = [3, 57, 1197, 25137]
  c2o = dict(zip(closers, openers))
  c2v = dict(zip(closers, cvalues))
  o2v = dict(zip(openers, ovalues))

  corrupted = []
  incomplete_scores = []
  for line in lines:
    stack = []
    corrupt = False
    for l in line:
      if l in openers:
        stack.append(l)
      else:
        if stack[-1] == c2o[l]:
          stack.pop()
        else:
          corrupt = True
          corrupted.append(l)
          break
    if not corrupt:
      score = 0
      for o in stack[::-1]:
        score *= 5
        score += o2v[o]
      incomplete_scores.append(score)

  return sum(map(lambda c: c2v[c], corrupted)), median(incomplete_scores)

def getInput(fn):
  with open(fn, 'r') as f:
    return f.read().splitlines()

def main():
  print(solve(getInput('input')))

if __name__ == '__main__':
  main()

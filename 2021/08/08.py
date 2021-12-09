#!/usr/bin/env python3

def makeLuts(patterns):
  luts = []
  patterns = [sorted(p, key=len) for p in patterns]
  for pattern in patterns:
    pattern = [''.join(sorted(p)) for p in pattern]
    p = [set(p) for p in pattern]
    lut = [-1] * 10
    lut[0] = 1
    lut[1] = 7
    lut[2] = 4
    lut[9] = 8
    for i in range(6, 9):
      if len(p[i] - p[1]) == 4:
        lut[i] = 6
      elif len(p[i] - p[2]) == 3:
        lut[i] = 0
      else:
        lut[i] = 9
    for i in range(3, 6):
      if len(p[i] - p[0]) == 3:
        lut[i] = 3
      elif len(p[i] - p[2]) == 2:
        lut[i] = 5
      else:
        lut[i] = 2
    luts.append(dict(zip(pattern, lut)))
  return luts

def solve(patterns, digits):
  p1 = sum([(sum(map(lambda d: 1 if len(d) <= 4 or len(d) == 7 else 0, d))) for d in digits])
  luts = makeLuts(patterns)
  p2 = sum([int(''.join(map(str, (map(lambda d: luts[i][''.join(sorted(d))], digits[i]))))) for i in range(len(patterns))])
  return p1, p2

def getInput(fn):
  with open(fn, 'r') as f:
    patterns = []
    digits = []
    for line in f.read().splitlines():
      p, d = line.split(' | ')
      patterns.append(p.split())
      digits.append(d.split()) 
    return patterns, digits

def main():
  patterns, digits = getInput('input')
  print(solve(patterns, digits))

if __name__ == '__main__':
  main()

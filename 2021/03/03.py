#!/usr/bin/env python3

def mostCommon(idx, lines):
  zeros = 0
  ones = 0
  for line in lines:
    if line[idx] == 1:
      ones += 1
    else:
      zeros += 1
  if zeros > ones:
    return 0
  return 1

def dec(bin_list):
  return int(''.join([str(x) for x in bin_list]), 2)

def findEntry(lines, invert=False):
  for i in range(len(lines[0])):
    next_lines = []
    common = mostCommon(i, lines)
    for line in lines:
      if (not invert and line[i] == common) or (invert and line[i] != common):
        next_lines.append(line)
    lines = next_lines
    if len(lines) == 1:
      return lines[0]
 

def solve(report):
  lines = []
  for line in report:
    lines.append([int(x) for x in line])
  gamma = []
  epsilon = []
  for i in range(len(lines[0])):
    if mostCommon(i, lines):
      gamma.append(1)
      epsilon.append(0)
    else:
      gamma.append(0)
      epsilon.append(1)
  gamma = dec(gamma)
  epsilon = dec(epsilon)

  oxygen = dec(findEntry(lines.copy()))
  co2 = dec(findEntry(lines.copy(), True))

  return gamma * epsilon, oxygen * co2


def getInput(fn):
  with open(fn, 'r') as f:
    return f.read().splitlines()

def main():
  print(solve(getInput('input')))

if __name__ == '__main__':
  main()

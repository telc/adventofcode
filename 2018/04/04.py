#!/usr/bin/env python2.7

import re
import operator

with open('input', 'r') as f:
  inputlines = f.read().splitlines()

#inputlines = """[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
#[1518-11-01 00:30] falls asleep
#[1518-11-01 00:55] wakes up
#[1518-11-01 23:58] Guard #99 begins shift
#[1518-11-02 00:40] falls asleep
#[1518-11-02 00:50] wakes up
#[1518-11-03 00:05] Guard #10 begins shift
#[1518-11-03 00:24] falls asleep
#[1518-11-03 00:29] wakes up
#[1518-11-04 00:02] Guard #99 begins shift
#[1518-11-04 00:36] falls asleep
#[1518-11-04 00:46] wakes up
#[1518-11-05 00:03] Guard #99 begins shift
#[1518-11-05 00:45] falls asleep
#[1518-11-05 00:55] wakes up""".splitlines()

def solve(inputlines):
  pat = re.compile('[\[\]]')
  d = dict([[l.strip() for l in filter(None, pat.split(line))] for line in inputlines])

  idx = None
  date = None
  start = 0
  stop = 0
  guards = {}
  for k in sorted(d.keys()):
    if d[k].find('Guard') != -1:
      idx = int(d[k].split()[1].strip('#'))
    elif d[k] == 'falls asleep':
      date = k[5:10]
      start = int(k[14:16])
    elif d[k] == 'wakes up':
      stop = int(k[14:16])
      if not idx in guards:
        guards[idx] = [0] * 60
      for i in xrange(start, stop):
        guards[idx][i] += 1

  s1id = 0
  s1sum = 0
  s1min = 0
  s2id = 0
  s2max = 0
  s2min = 0
  for g in guards:
    s = sum(guards[g])
    tmpmin, tmpmax = max(enumerate(guards[g]), key=operator.itemgetter(1))
    if s > s1sum:
      s1id = g
      s1sum = s
      s1min = tmpmin
    if tmpmax > s2max:
      s2id = g
      s2max = tmpmax
      s2min = tmpmin

  return s1id * s1min, s2id * s2min

if __name__ == '__main__':
  print solve(inputlines)

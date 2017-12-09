#!/usr/bin/env python

stream = open('input').read()
tests = [("{}", (1, 0)),
         ("{{{}}}", (6, 0)),
         ("{{},{}}", (5, 0)),
         ("{{{},{},{{}}}}", (16, 0)),
         ("{<a>,<a>,<a>,<a>}",(1, 4)),
         ("{{<ab>},{<ab>},{<ab>},{<ab>}}",(9,8)),
         ("{{<!!>},{<!!>},{<!!>},{<!!>}}",(9,0)),
         ("{{<a!>},{<a!>},{<a!>},{<ab>}}",(3,17)),
         ("<>", (0, 0)),
         ("<random characters>", (0, 17)),
         ("<<<<>", (0, 3)),
         ("<{!>}>", (0, 2)),
         ("<!!>", (0, 0)),
         ("<!!!>>", (0, 0)),
         ("""<{o"i!a,<{i<a>""", (0, 10))]

def solve(stream):
  garbage = False
  skip = False
  group = 0
  score = 0
  g_count = 0
  for c in stream:
    if skip:
      skip = False
    elif c == '!':
      skip = True
    elif not garbage and c == '<':
      garbage = True
    elif garbage and c == '>':
      garbage = False
    elif not garbage and c == '{':
      group += 1
      score += group
    elif not garbage and c == '}':
      group -= 1
    elif garbage:
      g_count += 1
  return score, g_count

for test in tests:
  if solve(test[0]) != test[1]:
    print test, solve(test[0])

print solve(stream)

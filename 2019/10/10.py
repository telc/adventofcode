#!/usr/bin/env python2.7

import math
from collections import defaultdict
from itertools import chain, islice, izip_longest

input_ = """.#..#
.....
#####
....#
...##""".splitlines()

input_ = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""".splitlines()

input_ = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""".splitlines()

input_ = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""".splitlines()

input_ = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".splitlines()

with open('input', 'r') as f:
  input_ = f.read().splitlines()

input_ = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##""".splitlines()

def vector(a, b):
  dx = a[0] - b[0]
  dy = a[1] - b[1]
  dist  = (dx**2 + dy**2)**.5
  dx /= dist
  dy /= dist
  return round(dx, 8), round(dy, 8), dist

def angle(vec):
  return (math.degrees(math.atan2(vec[0], vec[1])) + 90) % 360

def solve(lines):
  astroids = []
  max_seen = 0
  for y in xrange(len(lines)):
    row = lines[y]
    for x in xrange(len(row)):
      if row[x] == '#':
        astroids.append((x,y))

  for a in astroids:
    others = defaultdict(list)
    for b in astroids:
      if a == b:
        continue
      dx, dy, dist = vector(a, b)
      others[(dx,dy)].append((dist, b))
    if len(others) > max_seen:
      max_seen = len(others)
      max_seen_at = a
      max_others = others

  print sorted(max_others.keys(), key=angle)
  targets = [max_others[vec] for vec in sorted(max_others.keys(), key=angle)]
  print targets
  exit()
  targets = filter(None, chain.from_iterable(izip_longest(*targets)))
  print targets
  target = next(islice(targets, 199, None))

  print target
  return max_seen, target[1][0]*100 + target[1][1]

if __name__ == '__main__':
  print solve(input_)

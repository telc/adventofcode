#!/usr/bin/env python2.7

from collections import defaultdict

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

def vector(a, b):
  dx = a[0] - b[0]
  dy = a[1] - b[1]
  dist  = (dx**2 + dy**2)**.5
  dx /= dist
  dy /= dist
  return round(dx, 8), round(dy, 8), dist

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

  return max_seen

if __name__ == '__main__':
  print solve(input_)

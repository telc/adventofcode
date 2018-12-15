#!/usr/bin/env python2.7

from collections import deque

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########""".splitlines()

#input_ = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######""".splitlines()

#input_ = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######""".splitlines()

def bfs(start, squares, goals):
  visited = [[False] * len(squares[l]) for l in xrange(len(squares))]
  check = deque([[start]])
  visited[start[0]][start[1]] = True
  while len(check):
    path = check.popleft()
    coord = path[-1]
    y, x = coord
    if coord in goals:
      return path
    for dy, dx in [(-1,0),(0,-1),(0,1),(1,0)]:
      if not squares[y+dy][x+dx] and not visited[y+dy][x+dx]:
        visited[y+dy][x+dx] = True
        check.append(path+[[y+dy, x+dx]])
  return []

def solve(input_):
  ordered_units = [[y, x, input_[y][x] == 'E', 200] for y in xrange(len(input_)) for x in xrange(len(input_[y])) if input_[y][x] in 'EG']
  POWER = 3
  part1 = None
  while True:
    units = [u[:] for u in ordered_units]
    squares = [[s != '.' for s in line] for line in input_]
    elf_lost = False
    rounds = 0
    while True:
      combat = False
      for unit in sorted(units[:]):
        if unit not in units:
          continue
        y, x, is_elf, hp = unit
        adj = [[y+dy, x+dx, not is_elf] for dy, dx in [(-1,0),(0,-1),(0,1),(1,0)]]
        attacks = [u for u in units if u[:3] in adj]
        if attacks:
          combat = True
        else:
          combat = False
          reachable = []
          for target in units:
            if target[2] != unit[2]:
              combat = True
              ty, tx = target[:2]
              target_adj = [[ty+dy, tx+dx] for dy, dx in [(-1,0),(0,-1),(0,1),(1,0)]]
              reachable.extend([t for t in target_adj if not squares[t[0]][t[1]]])
          if not combat:
            break
          if not reachable:
            continue
          mv = bfs([y,x], squares, reachable)
          if not mv:
            continue
          mv = mv[1]
          squares[y][x] = False
          y, x = unit[:2] = mv
          squares[y][x] = True
          adj = [[y+dy, x+dx, not is_elf] for dy, dx in [(-1,0),(0,-1),(0,1),(1,0)]]
          attacks = [u for u in units if u[:3] in adj]
        if attacks:
          weakest = min(attacks, key=lambda u:(u[3],u[0],u[1]))
          if is_elf:
            weakest[3] -= POWER
          else:
            weakest[3] -= 3
          if weakest[3] <= 0:
            if weakest[2]:
              elf_lost = True
              if POWER != 3:
                break
            units.remove(weakest)
            squares[weakest[0]][weakest[1]] = False
      if elf_lost and POWER != 3:
        break
      if not combat:
        break
      rounds += 1
    if POWER == 3:
      part1 = rounds * sum(u[3] for u in units)
    if not elf_lost:
      break
    POWER += 1
  return part1, rounds * sum(u[3] for u in units)

if __name__ == '__main__':
  print solve(input_)

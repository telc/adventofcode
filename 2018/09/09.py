#!/usr/bin/env python2.7

from collections import deque

input_ = """470 players; last marble is worth 72170 points"""
input_ = """9 players; last marble is worth 25 points"""

PLAYERS = 470
MARBLES = 72170

def solve(input_):
  marbles = deque([0])
  players = [0] * PLAYERS
  current = 0
  player = 0
  for m in xrange(1, MARBLES+1):
    if not m % 23 == 0:
      marbles.rotate(-1)
      marbles.append(m)
    else:
      marbles.rotate(7)
      players[player] += m + marbles.pop()
      marbles.rotate(-1)
    player += 1
    if player >= PLAYERS:
      player = 0
  return max(players)

if __name__ == '__main__':
  print solve(input_),
  MARBLES *= 100
  print solve(input_)

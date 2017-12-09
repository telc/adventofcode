#!/usr/bin/env python

import numpy as np
import itertools

commands = """rotate right 3 steps
swap letter b with letter a
move position 3 to position 4
swap position 0 with position 7
swap letter f with letter h
rotate based on position of letter f
rotate based on position of letter b
swap position 3 with position 0
swap position 6 with position 1
move position 4 to position 0
rotate based on position of letter d
swap letter d with letter h
reverse positions 5 through 6
rotate based on position of letter h
reverse positions 4 through 5
move position 3 to position 6
rotate based on position of letter e
rotate based on position of letter c
rotate right 2 steps
reverse positions 5 through 6
rotate right 3 steps
rotate based on position of letter b
rotate right 5 steps
swap position 5 with position 6
move position 6 to position 4
rotate left 0 steps
swap position 3 with position 5
move position 4 to position 7
reverse positions 0 through 7
rotate left 4 steps
rotate based on position of letter d
rotate left 3 steps
swap position 0 with position 7
rotate based on position of letter e
swap letter e with letter a
rotate based on position of letter c
swap position 3 with position 2
rotate based on position of letter d
reverse positions 2 through 4
rotate based on position of letter g
move position 3 to position 0
move position 3 to position 5
swap letter b with letter d
reverse positions 1 through 5
reverse positions 0 through 1
rotate based on position of letter a
reverse positions 2 through 5
swap position 1 with position 6
swap letter f with letter e
swap position 5 with position 1
rotate based on position of letter a
move position 1 to position 6
swap letter e with letter d
reverse positions 4 through 7
swap position 7 with position 5
swap letter c with letter g
swap letter e with letter g
rotate left 4 steps
swap letter c with letter a
rotate left 0 steps
swap position 0 with position 1
reverse positions 1 through 4
rotate based on position of letter d
swap position 4 with position 2
rotate right 0 steps
swap position 1 with position 0
swap letter c with letter a
swap position 7 with position 3
swap letter a with letter f
reverse positions 3 through 7
rotate right 1 step
swap letter h with letter c
move position 1 to position 3
swap position 4 with position 2
rotate based on position of letter b
reverse positions 5 through 6
move position 5 to position 3
swap letter b with letter g
rotate right 6 steps
reverse positions 6 through 7
swap position 2 with position 5
rotate based on position of letter e
swap position 1 with position 7
swap position 1 with position 5
reverse positions 2 through 7
reverse positions 5 through 7
rotate left 3 steps
rotate based on position of letter b
rotate left 3 steps
swap letter e with letter c
rotate based on position of letter a
swap letter f with letter a
swap position 0 with position 6
swap position 4 with position 7
reverse positions 0 through 5
reverse positions 3 through 5
swap letter d with letter e
move position 0 to position 7
move position 1 to position 3
reverse positions 4 through 7"""

def swapLetter(array, x, y):
  for i in range(len(array)):
    if array[i] == x:
      array[i] = y
    elif array[i] == y:
      array[i] = x

def swapPostion(array, x, y):
  tmp = array[x]
  array[x] = array[y]
  array[y] = tmp

def rotate(array, left, steps):
  if left:
    new = np.roll(array, steps * -1)
  else:
    new = np.roll(array, steps)
  while len(array) > 0:
    array.pop()
  for n in new:
    array.append(n)

def rotateOn(array, x):
  index = array.index(x)
  steps = 1 + index
  if index >= 4:
    steps += 1
  rotate(array, False, steps)

def reverse(array, x, y):
  rev = array[:x] + array[x:y+1][::-1] + array[y+1:]
  while len(array) > 0:
    array.pop()
  for r in rev:
    array.append(r)

def move(array, x, y):
  array.insert(y, array.pop(x))

org = list('abcdefgh')
for password in itertools.permutations(org):
  password = list(password)
  org = ''.join(password)
  for command in commands.split('\n'):
    c = command.split()
    if c[0] == 'swap' and c[1] == 'letter':
      swapLetter(password, c[2], c[5])
    if c[0] == 'swap' and c[1] == 'position':
      swapPostion(password, int(c[2]), int(c[5]))
    if c[0] == 'rotate' and c[1] == 'left':
      rotate(password, True, int(c[2]))
    if c[0] == 'rotate' and c[1] == 'right':
      rotate(password, False, int(c[2]))
    if c[0] == 'rotate' and c[1] == 'based':
      rotateOn(password, c[6])
    if c[0] == 'reverse':
      reverse(password, int(c[2]), int(c[4]))
    if c[0] == 'move':
      move(password, int(c[2]), int(c[5]))
  if ''.join(password) == 'fbgdceah':
    print org
    exit()

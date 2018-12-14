#!/usr/bin/env python2.7

def solve(input_):
  recipes = '37'
  p1 = 0
  p2 = 1
  part1 = int(input_)
  l = len(input_)
  while recipes[-l:] != input_ and recipes[-l-1:-1] != input_:
    new = ord(recipes[p1]) + ord(recipes[p2]) - 96
    recipes += str(new)
    p1 = (p1 + 1 + ord(recipes[p1])-48) % len(recipes)
    p2 = (p2 + 1 + ord(recipes[p2])-48) % len(recipes)
  return recipes[part1:part1+10], len(recipes) - l - (0 if recipes[-l:] == input_ else 1)

if __name__ == '__main__':
  print solve("360781")

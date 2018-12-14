#!/usr/bin/env python2.7

def solve(input_):
  recipes = [3, 7]
  p1 = 0
  p2 = 1
  part2 = map(int, list(str(input_)))
  while recipes[-len(part2):] != part2 and recipes[-len(part2)-1:-1] != part2:
    new = recipes[p1] + recipes[p2]
    recipes += map(int, list(str(new)))
    p1 = (p1 + 1 + recipes[p1]) % len(recipes)
    p2 = (p2 + 1 + recipes[p2]) % len(recipes)
  return ''.join(map(str, recipes[input_:input_+10])), len(recipes) - len(part2) - (0 if recipes[-len(part2):] == part2 else 1)


if __name__ == '__main__':
  print solve(360781)

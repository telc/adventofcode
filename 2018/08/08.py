#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = f.read().strip()

#input_ = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

def parseNode(data):
  num_children = data[0]
  num_meta = data[1]
  i = 2
  meta = 0
  value = 0
  children = []
  for c in xrange(num_children):
    p, sub_meta, sub_value = parseNode(data[i:])
    i += p
    meta += sub_meta
    children.append(sub_value)
  meta += sum(data[i:i+num_meta])
  if num_children > 0:
    for m in data[i:i+num_meta]:
      m -= 1
      if m >= 0 and m < len(children):
        value += children[m]
  else:
    value = meta
  i += num_meta
  return i, meta, value


def solve(input_):
  data = map(int, input_.split())
  return parseNode(data)[1:]

if __name__ == '__main__':
  print solve(input_)

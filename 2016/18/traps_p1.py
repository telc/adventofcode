#!/usr/bin/env python

input = '..^^.'
input = '.^^.^.^^^^'
input = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'

def makeRow(row):
  ret = ''
  row = '.' + row + '.'
  for i in range(len(row) - 2):
    r = row[i:i+3]
    if r == '^^.' or r == '.^^' or r == '^..' or r == '..^':
      ret += '^'
    else:
      ret += '.'
  return ret

rows = [input]

while len(rows) < 40:
  rows.append(makeRow(rows[-1]))

s = 0
for row in rows:
  s += row.count('.')
print s

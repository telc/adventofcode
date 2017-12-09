#!/usr/bin/env python

import md5
if __name__ == '__main__':
  inp = "yzbqklnj"
  c = 0
  while True:
    c += 1
    m = md5.new()
    m.update(inp + str(c))
    if m.hexdigest()[:6] == '000000':
      break
  print c

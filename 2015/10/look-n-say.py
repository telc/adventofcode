#!/usr/bin/env python

def lookAndSay(num):
  ret = ""
  count = 0
  cur = num[0]
  for i in range(len(num)):
    if num[i] == cur:
      count += 1
    else:
      ret += str(count)
      ret += cur
      count = 1
      cur = num[i]
  ret += str(count)
  ret += cur
  return ret

if __name__ == '__main__':
  inp = "1321131112"

  num = inp
  for i in range(50):
    num = lookAndSay(num)
  print len(num)

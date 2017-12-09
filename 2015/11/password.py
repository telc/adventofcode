#!/usr/bin/env python

max_char = ord('z')

def incrementPassword(password):
  slot = -1
  p = list(password)
  while ord(p[slot])+1 > max_char:
    p[slot] = 'a'
    slot -= 1
  p[slot] = chr(ord(p[slot])+1)
  return ''.join(p)

def validPassword(password):
  has_straight = False
  has_double = False
  if 'i' in password or 'o' in password or 'l' in password:
    return False

  for i in range(len(password)-1):
    pair = password[i:i+2]
    if i < len(password)-2:
      if ord(password[i]) == ord(password[i+1])-1 and ord(password[i+1]) == ord(password[i+2])-1:
        has_straight = True
    for j in range(i+2, len(password)-1):
      pair2 = password[j:j+2]
      if pair[0] == pair[1] and pair2[0] == pair2[1]:
        has_double = True

  return has_straight and has_double

if __name__ == '__main__':
  inp = "vzbxkghb"

  new = incrementPassword(inp)
  while not validPassword(new):
    new = incrementPassword(new)

  print new

  new = incrementPassword(new)
  while not validPassword(new):
    new = incrementPassword(new)

  print new

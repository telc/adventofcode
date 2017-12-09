#!/usr/bin/env python

data = '11011110011011101'

def flip(bits):
  ret = ''
  for b in bits:
    if b == '0':
      ret += '1'
    else:
      ret += '0'
  return ret

def dragon(a):
  b = a[::-1]
#  b = bin(int(b,2) ^ int('1'*len(b),2))[2:]
  b = flip(b)
  return a + '0' + b

def checksum(data):
  ret = ''
  for i in range(0, len(data), 2):
    if data[i] == data[i+1]:
      ret += '1'
    else:
      ret += '0'
  return ret

while len(data) < 272:
  data = dragon(data)
data = data[:272]

check = checksum(data)
while len(check) % 2 == 0:
  check = checksum(check)
print check

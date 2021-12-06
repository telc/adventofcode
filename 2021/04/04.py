#!/usr/bin/env python3

def clearValue(board, n):
  for y in range(len(board)):
    for x in range(len(board[0])):
      if board[y][x] == n:
        board[y][x] = 0
        return

def sumRow(board, row):
  return sum(board[row]) - len(board[row]) + board[row].count(0)

def sumBoard(board):
  return sum([sumRow(board, row) for row in range(len(board))])

def hasBingo(board):
  for row in range(len(board)):
    if sum(board[row]) == 0:
      return True
  col_sums = [sum(x) for x in zip(*board)]
  if col_sums.count(0) > 0:
    return True
  return False


def solve(numbers, boards, last=False):
  for n in numbers:
    for board in boards.copy():
      clearValue(board, n)
      if hasBingo(board):
        if last and len(boards) > 1:
          boards.remove(board)
        else:
          return sumBoard(board) * (n - 1)

def makeBoard(lines):
  rows = [[int(x)+1 for x in line.split()] for line in lines]
  return rows

def getInput(fn):
  lines = []
  with open(fn, 'r') as f:
    lines = f.read().splitlines()
  numbers = [int(x)+1 for x in lines[0].split(',')]
  boards = []
  for l in range(2, len(lines), 6):
    boards.append(makeBoard(lines[l:l+5]))
  return numbers, boards

def main():
  numbers, boards = getInput('input')
  print(solve(numbers, boards))
  print(solve(numbers, boards, True))

if __name__ == '__main__':
  main()

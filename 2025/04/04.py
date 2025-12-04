#!/usr/bin/env python

with open('input', 'r') as f:
    input_ = [[y for y in x] for x in f.read().splitlines()]

with open('test', 'r') as f:
    test_ = [[y for y in x] for x in f.read().splitlines()]

def num_neighbours(grid: list[list[str]], row: int, col: int):
    neighbours = 0
    for y in range(row-1, row+2):
        if y < 0 or y >= len(grid):
            continue
        for x in range(col-1, col+2):
            if x < 0 or x >= len(grid) or (y == row and x == col):
                continue
            if (grid[y][x] != '.'):
                neighbours += 1
    return neighbours

def remove_accessable(grid: list[list[str]], insert: str = 'x'):
    removed = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@' and num_neighbours(grid, y, x) < 4:
                grid[y][x] = insert
                removed += 1
    return removed

def cleanup(grid: list[list[str]]):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'x':
                grid[y][x] = '.'

def p1(grid: list[list[str]]):
    return remove_accessable(grid, '@') # We need to preserve the grid for p2()

def p2(grid: list[list[str]]):
    removed = 0
    while True:
        new_removed = remove_accessable(grid)
        if new_removed == 0:
            break
        removed += new_removed
        cleanup(grid)
    return removed

if __name__ == '__main__':
    print(p1(input_))
    print(p2(input_))

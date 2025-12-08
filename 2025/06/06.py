#!/usr/bin/env python

import sys
from functools import reduce

def init(filename: str, p1 = True):
    with open(filename, 'r') as f:
        if p1:
            matrix = [x.split() for x in f.read().splitlines()]
            for i in range(len(matrix) - 1):
                matrix[i] = [int(x) for x in matrix[i]]
            return [list(row) for row in zip(*reversed(matrix))]
        matrix = []
        lines = f.read().splitlines()
        num_digits = len(lines) - 1
        for col in range(len(lines[0])):
            if lines[num_digits][col] != ' ':
                matrix.append([lines[num_digits][col]])
            col_digit = 0
            if lines[0][col] != ' ':
                col_digit += int(lines[0][col])
            if lines[1][col] != ' ':
                col_digit *= 10
                col_digit += int(lines[1][col])
            if lines[2][col] != ' ':
                col_digit *= 10
                col_digit += int(lines[2][col])
            if num_digits == 4 and lines[3][col] != ' ':
                col_digit *= 10
                col_digit += int(lines[3][col])
            if col_digit > 0:
                matrix[-1].append(col_digit)
        return matrix

def calc_row(row: list):
    if row[0] == '*':
        return reduce(lambda x, y: x * y, row[1:], 1)
    return reduce(lambda x, y: x + y, row[1:])

def sum_matrix(matrix: list[list]):
    sum = 0
    for row in matrix:
        sum += calc_row(row)
    print(sum)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    p1_matrix = init(filename)
    p2_matrix = init(filename, False)
    sum_matrix(p1_matrix)
    sum_matrix(p2_matrix)

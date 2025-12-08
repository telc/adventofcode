#!/usr/bin/env python

import sys

def init(filename: str):
    with open(filename, 'r') as f:
        return [list(x) for x in f.read().splitlines()]

def p1(diagram: list[list[str]]):
    beams = set()
    splits = 0
    for line in diagram:
        for i, c in enumerate(line):
            if c == 'S':
                beams.add(i)
            if c == '^' and i in beams:
                beams.remove(i)
                beams.add(i-1)
                beams.add(i+1)
                splits += 1
    print(splits)

def p2(diagram: list[list[str]]):
    start_pos = None
    for i, c in enumerate(diagram[0]):
        if c == 'S':
            start_pos = i
            break

    # Key: column position, Value: number of timelines with particle at that position
    positions = {start_pos: 1}

    for row in diagram:
        new_positions = {}
        for pos, count in positions.items():
            if row[pos] == '^':
                new_positions[pos-1] = new_positions.get(pos-1, 0) + count
                new_positions[pos+1] = new_positions.get(pos+1, 0) + count
            else:
                new_positions[pos] = new_positions.get(pos, 0) + count
        positions = new_positions

    print(sum(positions.values()))

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    diagram = init(filename)
    p1(diagram)
    p2(diagram)

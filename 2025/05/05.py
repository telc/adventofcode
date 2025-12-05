#!/usr/bin/env python

import sys

def combine_fresh(old_fresh: list[list[int]]):
    new_fresh = list()
    for low, high in old_fresh:
        updated = False
        for i in range(len(new_fresh)):
            if max(low, new_fresh[i][0]) <= min(high, new_fresh[i][1]):
                new_fresh[i][0] = min(low, new_fresh[i][0])
                new_fresh[i][1] = max(high, new_fresh[i][1])
                updated = True
                break
        if not updated:
            new_fresh.append([low, high])
    return new_fresh

def init(filename: str):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        sep_pos = lines.index('')
        fresh = [list(map(int, x.split('-'))) for x in lines[:sep_pos]]
        available = [int(x) for x in lines[sep_pos+1:]]
    while True:
        new_fresh = combine_fresh(fresh)
        if len(fresh) == len(new_fresh):
            break
        fresh = new_fresh
    return fresh, available

def num_fresh_available(fresh, available):
    num_fresh = 0
    for id in available:
        for low, high in fresh:
            if id >= low and id <= high:
                num_fresh += 1
                break
    return num_fresh

def num_fresh_ids_total(fresh):
    num_ids = 0
    for low, high in fresh:
        num_ids += high - low + 1
    return num_ids

def p1(fresh, available):
    print(num_fresh_available(fresh, available))

def p2(fresh):
    print(num_fresh_ids_total(fresh))

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    fresh, available = init(filename)
    p1(fresh, available)
    p2(fresh)

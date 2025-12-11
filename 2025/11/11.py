#!/usr/bin/env python

import sys

def init(filename: str):
    with open(filename, 'r') as f:
        return {x.split(':')[0]: x.split()[1:] for x in f.read().splitlines()}
    
def find_paths(graph: dict[str, list[str]], start: str, end: str, memo: dict = None) -> int:
    if memo is None:
        memo = {}

    if (start, end) in memo:
        return memo[(start, end)]

    if start == end:
        return 1
    if start not in graph:
        return 0

    paths = 0
    for node in graph[start]:
        paths += find_paths(graph, node, end, memo)

    memo[(start, end)] = paths
    return paths

def p1(graph: dict[str, list[str]]):
    print(find_paths(graph, 'you', 'out'))

def p2(graph: dict[str, list[str]]):
    fft_first = find_paths(graph, 'svr', 'fft') * find_paths(graph, 'fft', 'dac') * find_paths(graph, 'dac', 'out')
    dac_first = find_paths(graph, 'svr', 'dac') * find_paths(graph, 'dac', 'fft') * find_paths(graph, 'fft', 'out')
    print(fft_first + dac_first)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    graph = init(filename)
    p1(graph)
    if (filename == 'test'):
        graph = init('test2')
    p2(graph)

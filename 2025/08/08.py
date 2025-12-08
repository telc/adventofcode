#!/usr/bin/env python

import sys
import math

def init(filename: str):
    with open(filename, 'r') as f:
        return [tuple(map(int, x.split(','))) for x in f.read().splitlines()]

def distance(p: tuple[int, int, int], q: tuple[int, int, int]):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)

def make_circuits(nodes: list[tuple[int,int,int]], num_edges: int = 0):
    parent = list(range(len(nodes)))

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    def count_circuits() -> int:
        return len(set(find(i) for i in range(len(nodes))))

    # Pre-compute all pairs and their distances, then sort by distance
    pairs = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            dist = distance(nodes[i], nodes[j])
            pairs.append((dist, i, j))
    pairs.sort()

    # Add edges, skipping pairs already in same circuit
    edges_checked = 0
    last_connection = None
    for dist, i, j in pairs:
        if num_edges > 0 and edges_checked >= num_edges:
            break
        edges_checked += 1
        if find(i) != find(j):
            union(i, j)
            last_connection = (i, j)
            if num_edges < 0 and count_circuits() == 1:
                break

    # Group nodes by their circuit
    circuits = {}
    for i in range(len(nodes)):
        root = find(i)
        if root not in circuits:
            circuits[root] = []
        circuits[root].append(i)

    return list(circuits.values()), last_connection

def p1(nodes: list[tuple[int,int,int]], num_edges: int):
    circuits, _ = make_circuits(nodes, num_edges=num_edges)
    sizes = [len(circuit) for circuit in circuits]
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

def p2(nodes: list[tuple[int,int,int]], num_edges: int):
    _, last_connection = make_circuits(nodes, num_edges=-1)
    i, j = last_connection
    print(nodes[i][0] * nodes[j][0])

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    nodes = init(filename)
    p1(nodes, 10 if filename == 'test' else 1000)
    p2(nodes, 0)

#!/usr/bin/env python

import sys

def init(filename: str):
    with open(filename, 'r') as f:
        return [tuple(map(int, x.split(','))) for x in f.read().splitlines()]
    
def area(p: tuple[int, int], q: tuple[int, int]):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)
    
def p1(polygon: list[tuple[int,int]]):
    largest = 0
    for i in range(len(polygon)):
        for j in range(i+1, len(polygon)):
            a = area(polygon[i], polygon[j])
            largest = max(largest, a)
    print(largest)

def is_rectangle_valid(x_min, x_max, y_min, y_max, edge_data):
    corners = ((x_min, y_min), (x_max, y_max), (x_min, y_max), (x_max, y_min))

    # Check if any edge passes through the rectangle interior
    for p1, p2, is_vertical, ex_min, ex_max, ey_min, ey_max in edge_data:
        # Skip if both endpoints are rectangle corners (this is allowed)
        if p1 in corners and p2 in corners:
            continue

        # Quick bounding box check - skip if edge doesn't overlap rectangle
        if ex_max < x_min or ex_min > x_max or ey_max < y_min or ey_min > y_max:
            continue

        # Check if edge has a point strictly inside the rectangle
        if is_vertical:
            x = p1[0]
            if x_min < x < x_max and ey_min < y_max and ey_max > y_min:
                return False
        else:
            y = p1[1]
            if y_min < y < y_max and ex_min < x_max and ex_max > x_min:
                return False
    return True

def p2(polygon: list[tuple[int,int]]):
    # Generate all rectangles and sort by area (descending)
    n = len(polygon)
    rectangles = []
    for i in range(n):
        for j in range(i+1, n):
            a = area(polygon[i], polygon[j])
            rectangles.append((a, i, j))
    rectangles.sort(reverse=True)

    # Precompute edge and bounding box data
    edge_data = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        is_vertical = (p1[0] == p2[0])
        ex_min = min(p1[0], p2[0])
        ex_max = max(p1[0], p2[0])
        ey_min = min(p1[1], p2[1])
        ey_max = max(p1[1], p2[1])
        edge_data.append((p1, p2, is_vertical, ex_min, ex_max, ey_min, ey_max))

    # Find largest valid rectangle
    largest = 0
    for a, i, j in rectangles:
        if a <= largest:
            break

        p1, p2 = polygon[i], polygon[j]
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

        if is_rectangle_valid(x_min, x_max, y_min, y_max, edge_data):
            largest = a

    print(largest)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    polygon = init(filename)
    p1(polygon)
    p2(polygon)

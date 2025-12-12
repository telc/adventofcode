#!/usr/bin/env python

import sys

def init(filename: str):
    with open(filename, 'r') as f:
        blocks = f.read().strip().split('\n\n')

    shape_data = {int(b.split('\n')[0].split(':')[0]): {(r, c) for r, line in enumerate(b.split('\n')[1:])
                  for c, ch in enumerate(line) if ch == '#'} for b in blocks if b.split('\n')[0].split(':')[0].isdigit()}
    shapes = [shape_data[i] for i in sorted(shape_data.keys())]

    trees = [(*map(int, line.split(':')[0].split('x')), list(map(int, line.split(':')[1].split())))
             for b in blocks if 'x' in b.split('\n')[0] for line in b.split('\n')]

    return shapes, trees

def rotate_90(coords: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {(c, -r) for r, c in coords}

def flip_horizontal(coords: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {(r, -c) for r, c in coords}

def normalize(coords: set[tuple[int, int]]) -> set[tuple[int, int]]:
    if not coords:
        return coords
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return {(r - min_r, c - min_c) for r, c in coords}

def get_all_transformations(coords: set[tuple[int, int]]) -> list[set[tuple[int, int]]]:
    transformations = set()

    current = coords
    for _ in range(4):
        transformations.add(frozenset(normalize(current)))
        transformations.add(frozenset(normalize(flip_horizontal(current))))
        current = rotate_90(current)

    return [set(t) for t in transformations]

def solve_placement(width: int, height: int, presents: list[list[set[tuple[int, int]]]]) -> bool:
    if not presents:
        return True

    # Early termination: check if total cells needed > available cells
    total_cells_needed = sum(len(trans[0]) for trans in presents if trans)
    if total_cells_needed > width * height:
        return False

    # Filter out empty present lists and sort by size (largest first)
    presents_filtered = [p for p in presents if p]
    presents_sorted = sorted(presents_filtered, key=lambda p: -len(p[0]))

    grid = [[False] * width for _ in range(height)]

    def backtrack(idx: int) -> bool:
        if idx == len(presents_sorted):
            return True

        # Try each transformation
        for transformation in presents_sorted[idx]:
            # Compute bounds once per transformation
            max_r = max(r for r, c in transformation)
            max_c = max(c for r, c in transformation)

            # Try all valid positions
            for start_r in range(height - max_r):
                for start_c in range(width - max_c):
                    # Check if can place
                    can_place_here = True
                    for dr, dc in transformation:
                        if grid[start_r + dr][start_c + dc]:
                            can_place_here = False
                            break

                    if can_place_here:
                        # Place
                        for dr, dc in transformation:
                            grid[start_r + dr][start_c + dc] = True

                        if backtrack(idx + 1):
                            return True

                        # Unplace
                        for dr, dc in transformation:
                            grid[start_r + dr][start_c + dc] = False

        return False

    return backtrack(0)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    shapes, trees = init(filename)

    shape_permutations = []
    for shape in shapes:
        shape_permutations.append(get_all_transformations(shape))

    solvable_count = 0

    for width, height, counts in trees:
        presents = []
        for shape_idx, count in enumerate(counts):
            for _ in range(count):
                if shape_idx < len(shape_permutations):
                    presents.append(shape_permutations[shape_idx])

        if solve_placement(width, height, presents):
            solvable_count += 1

    print(solvable_count)

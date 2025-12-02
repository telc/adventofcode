#!/usr/bin/env python

with open('input', 'r') as f:
    input_ = [(-1 if x[0] == 'L' else 1) * int(x[1:]) for x in f.read().splitlines()]

with open('test', 'r') as f:
    test_ = [(-1 if x[0] == 'L' else 1) * int(x[1:]) for x in f.read().splitlines()]

def p1(rotations):
    position = 50
    count = 0
    for rotation in rotations:
        position = (position + rotation) % 100
        if position == 0:
            count += 1
    return count

def p2(rotations):
    position = 50
    count = 0
    for rotation in rotations:
        if rotation >= 0:
            count += (position + rotation) // 100
        else:
            dist = -rotation
            if position > 0 and dist >= position:
                # We cross 0, then possibly multiple more times
                count += 1 + (dist - position) // 100
            elif position == 0:
                # Starting at 0, we only cross after a full rotation
                count += dist // 100
        position = (position + rotation) % 100
    return count

if __name__ == '__main__':
    print(p1(input_))
    print(p2(input_))

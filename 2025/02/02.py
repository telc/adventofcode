#!/usr/bin/env python

with open('input', 'r') as f:
    input_ = [tuple(map(int, x.split('-'))) for x in f.read().strip().split(',')]

with open('test', 'r') as f:
    test_ = [tuple(map(int, x.split('-'))) for x in f.read().strip().split(',')]

def is_invalid_id(num, exactly_twice=False):
    s = str(num)
    length = len(s)

    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            repetitions = length // pattern_length
            pattern = s[:pattern_length]
            if pattern * repetitions == s:
                if exactly_twice and repetitions == 2:
                    return True
                elif not exactly_twice and repetitions >= 2:
                    return True
    return False

def sum_invalid_ids(ranges, exactly_twice=False):
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num, exactly_twice):
                total += num
    return total

def p1(ranges):
    return sum_invalid_ids(ranges, exactly_twice=True)

def p2(ranges):
    return sum_invalid_ids(ranges, exactly_twice=False)

if __name__ == '__main__':
    print(p1(input_))
    print(p2(input_))

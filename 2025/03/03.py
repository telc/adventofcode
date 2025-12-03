#!/usr/bin/env python

with open('input', 'r') as f:
    input_ = [x for x in f.read().splitlines()]

with open('test', 'r') as f:
    test_ = [x for x in f.read().splitlines()]

def find_highest_joltage(bank: str, num_bat: int):
    joltage = ''
    current_pos = 0

    for i in range(num_bat):
        max_search_pos = len(bank) - num_bat + i + 1
        segment = bank[current_pos:max_search_pos]
        best_digit = max(segment)
        best_pos = current_pos + segment.index(best_digit)

        joltage += best_digit
        current_pos = best_pos + 1

    return int(joltage)

def sum_joltage(banks: list[str], num_bat: int):
    output = 0
    for bank in banks:
        output += find_highest_joltage(bank, num_bat)
    return output

def p1(banks: list[str]):
    return sum_joltage(banks, 2)

def p2(banks: list[str]):
    return sum_joltage(banks, 12)

if __name__ == '__main__':
    print(p1(input_))
    print(p2(input_))

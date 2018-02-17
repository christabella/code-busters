#!/usr/bin/env python
'''The idea is that we can greedily determine whether a flip needs to be
made at each position in order for the pancakes to be happy.'''
import itertools


def all_combinations(l):
    all_lengths = range(0, len(l)+1)
    return itertools.chain.from_iterable(
        itertools.combinations(l, i)
        for i in all_lengths
    )


def flip(pancakes, position, flipper_size):
    ''' Position to start flipping from '''
    right_pos = position + flipper_size
    flipped = ''.join(
        ['+' if p == '-' else '-' for p in pancakes[position:right_pos]]
    )
    return pancakes[:position] + flipped + pancakes[right_pos:]


def is_happy(pancakes):
    return pancakes == "+" * len(pancakes)


def solve(pancakes, flipper_size):
    flips = 0
    for pos in range(len(pancakes) - flipper_size + 1):
        if (pancakes[pos]) == '-':
            pancakes = flip(pancakes, pos, flipper_size)
            flips += 1
    if is_happy(pancakes):
        return flips
    return "IMPOSSIBLE"


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        pancakes, flipper = input().split()
        print("Case #{}: {}".format(case, solve(pancakes, int(flipper))))

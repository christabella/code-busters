#!/usr/bin/env python
import itertools
'''Naive implementation where we literally go through the motions'''

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
    # All possible flip combinations sorted in increasing length
    all_flip_combinations = all_combinations(range(len(pancakes) - flipper_size + 1))
    for flips in all_flip_combinations:
        hypothesis_pancakes = pancakes
        for pos in flips:
            hypothesis_pancakes = flip(hypothesis_pancakes, pos, flipper_size)

        if is_happy(hypothesis_pancakes):
            return len(flips)
    return "IMPOSSIBLE"


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        pancakes, flipper = input().split()
        print("Case #{}: {}".format(case, solve(pancakes, int(flipper))))

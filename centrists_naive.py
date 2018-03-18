#!/usr/bin/env python

import itertools
'''
https://code.google.com/codejam/contest/8384486/dashboard#s=p2&a=2
Brute force solution
'''

def solve(l, names):
    alphabet = set(''.join(names))
    A = len(alphabet)
    bools = [False] * 3
    # Try all N! (for small dataset, 3!) alphabetical orderings
    for ordering in itertools.permutations(range(A), A):
        hashmap = dict(zip(alphabet, ordering))
        # Order the names
        ordered_names = list(enumerate([list(map(lambda x: hashmap[x], name)) for name in names]))
        ordered_names.sort(key=lambda x: x[1])
        mid_idx = ordered_names[1][0]
        bools[mid_idx] = True
    return " ".join(["YES" if bool else "NO" for bool in bools])


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        l = int(input())
        names = input().split()
        print("Case #{}: {}".format(case, solve(l, names)))

'''
python3 centrists.py < C-small-attempt0.in > out-
diff out- out-C-small

'''

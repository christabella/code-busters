#!/usr/bin/env python

from collections import Counter
'''
You forgot the situation where 1 letter is different (Ld) and 2 letters are the same (Ls), 
and at the next index where the 2 are different, their values are Ld and Ls.

ABA, ABC, CCC

Ld = C at position 0
Ls = A at position 0

L1 = A at position 2
L2 = C at position 2

If A > C (in the alphabetical order):
CCC, ABC, ABA

Else, if A < C:
ABA, ABC, CCC

So ABA can never be in the middle!!!!!!!
'''

def get_pos_odd(letters):
    counter = Counter(letters)
    return letters.index(min(counter, key=counter.get))

def solve(l, names):
    bools = [True] * 3
    i = 0
    for i in range(l):
        letters = [name[i] for name in names]
        unique_letters = set(letters)
        if len(unique_letters) == 1:  # All the same
            continue
        elif len(unique_letters) == 2:  # One needs to be struck out
            if bools[get_pos_odd(letters)] == True and sum(bools) < 3:
                bools[get_pos_odd(letters)] = False
                return " ".join(["YES" if bool else "NO" for bool in bools])
            else:
                bools[get_pos_odd(letters)] = False
        elif len(unique_letters) == 3:
            return "YES YES YES"

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

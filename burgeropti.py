#!/usr/bin/env python
'''https://code.google.com/codejam/contest/8384486/dashboard#s=p0&a=0'''


def smallest_error(k, d):
    d = sorted(d)
    err = 0
    for i in range(k):
        # Put smallest values closer to bun at position i//2
        pos = i//2
        err += (d[i] - pos)**2
    return err


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        k = int(input())
        d = [int(x) for x in input().split()]
        print("Case #{}: {}".format(case, smallest_error(k, d)))

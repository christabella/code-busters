#!/usr/bin/env python
# https://code.google.com/codejam/contest/32013/dashboard


def process_queries(s, S, q, Q):
    d = dict()  # A dict of encountered search engines so far
    switches = 0
    for qy in Q:
        # Check if this has already been encountered
        if qy in d:
            continue
        else:
            # If d is maxed out, reset d and increment switches
            if len(d) == s - 1:
                switches += 1
                d = dict()
            d[qy] = 1
    return switches


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        s = int(input())
        S = []
        for _ in range(s):
            S.append(input())
        q = int(input())
        Q = []
        for _ in range(q):
            Q.append(input())
        print("Case #{}: {}".format(case, process_queries(s, S, q, Q)))

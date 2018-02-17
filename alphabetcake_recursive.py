#!/usr/bin/env python
import numpy as np

def find_corners(cake, initial):
    row_indices = []
    col_indices = []
    for r, row in enumerate(cake):
        for c, char in enumerate(row):
            if char == initial:
                row_indices.append(r)
                col_indices.append(c)
    return (min(row_indices), min(col_indices)), (max(row_indices), max(col_indices))

def fill_cake(cake):
    # Plug the holes
    initials = []
    if len(cake) == 0:
        return ""
    for r, row in enumerate(cake):
        for c, char in enumerate(row):
            if char != "?":
                initials.append([char, r, c])
    if len(initials) == 1:
        # return cake.fill(initials[0][0])
        return np.full(cake.shape, initials[0][0], dtype=str)
    i1, r1, c1 = initials[0]
    i2, r2, c2 = initials[1]
    if r1 != r2:
        if r1 > r2:
            # Split into top and bottom
            # index is comma separated for multidimensional arrays
            # first 0::1 is for which rows u wanna select;
            #     second :: is for which cols
            # r1 > r2
            top = fill_cake(cake[:r2+1, :])
            bottom = fill_cake(cake[r2+1:, :])
            return np.r_[top, bottom]
        elif r1 < r2:
            top = fill_cake(cake[:r1+1, :])
            bottom = fill_cake(cake[r1+1:, :])
            return np.r_[top, bottom]

    else:
        if c1 > c2:
            left = fill_cake(cake[:, :c2+1])
            right = fill_cake(cake[:, c2+1:])
            return np.c_[left, right]
        elif c2 > c1:
            left = fill_cake(cake[:, :c1+1])
            right = fill_cake(cake[:, c1+1:])
            return np.c_[left, right]
    # top_left, bottom_right = find_corners(cake, initial)
    # this cake filling approach won't work because it's
    # So many edge cases
    # cake = fill_portion(cake, top_left, bottom_right)
    # Colour in the rest according to any neighbour


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        R, C = [int(x) for x in input().split()]
        cake = []
        for r in range(R):
            cake.append(list(input()))
        cake = fill_cake(np.array(cake))
        # print(cake)
        cakestring = '\n'.join([''.join([str(x[0]) for x in row]) for row in cake])
        print("Case #{}:\n{}".format(case, cakestring))

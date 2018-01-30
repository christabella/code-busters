#!/usr/bin/env python3


def get_items_to_buy(items, credit):
    for a_idx, a in enumerate(items):
        for b_idx, b in enumerate(items):
            if a_idx != b_idx and a + b == credit:
                return a_idx+1, b_idx+1


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        credit = int(input())
        num_items = int(input())
        items = [int(x) for x in input().split()]
        print("Case #{}: {} {}".format(case, *get_items_to_buy(items, credit)))

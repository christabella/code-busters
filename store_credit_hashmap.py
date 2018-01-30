#!/usr/bin/env python3


def get_items_to_buy(items, credit):
    MAX_NUM = 2000
    found_map = ["not_found"]*MAX_NUM

    for i in range(0, len(items)):
        complement = credit - items[i]
        if (complement >= 0 and found_map[complement] != "not_found"):
            # The complement had been found already!
            return [found_map[complement]+1, i+1]
        # Oh well, just store the index of this number
        found_map[items[i]] = i


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        credit = int(input())
        num_items = int(input())
        items = [int(x) for x in input().split()]
        print("Case #{}: {} {}".format(case, *get_items_to_buy(items, credit)))

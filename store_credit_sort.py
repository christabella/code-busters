#!/usr/bin/env python3


def get_items_to_buy(items, credit):
    indices, items = zip(*sorted(enumerate(items), key=lambda x: x[1]))

    i = 0
    j = len(items) - 1
    current_sum = items[i] + items[j]
    while current_sum != credit:
        if current_sum < credit:
            i += 1
        elif current_sum > credit:
            j -= 1
        current_sum = items[i] + items[j]

    return sorted([indices[i]+1, indices[j]+1])


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        credit = int(input())
        num_items = int(input())
        items = [int(x) for x in input().split()]
        print("Case #{}: {} {}".format(case, *get_items_to_buy(items, credit)))

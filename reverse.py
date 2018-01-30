#!/usr/bin/env python3


def reverse_words(string):
    words = string.split()
    return ' '.join(words[::-1])


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        string = input()
        print("Case #{}: {}".format(case, reverse_words(string)))

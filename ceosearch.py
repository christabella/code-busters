#!/usr/bin/env python
'''https://code.google.com/codejam/contest/8384486/dashboard#s=a&a=1'''


def min_ceo_exp(employees, l):
    employees = sorted(employees, key=lambda x: x[1])
    # CEO must be greater than this
    max_num, max_exp = employees[-1]
    starting = max(max_num, max_exp+1)
    # These people need to be managed
    lower_ranks = employees[0][0]
    for i in range(1, l):
        # number of lowest experience employees
        num, exp = employees[i]
        # This rank take as much as possible
        lower_ranks -= num * exp
        # Add this rank to the lower_ranks
        lower_ranks += num
    return max(lower_ranks, starting)


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        l = int(input())
        employees = []
        for _ in range(l):
            employees.append([int(x) for x in input().split()])
        print("Case #{}: {}".format(case, min_ceo_exp(employees, l)))

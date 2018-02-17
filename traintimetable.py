#!/usr/bin/env python
from datetime import datetime, timedelta
from heapq import heappush, heappop
'''
Greedy approach with 2 min heaps (`trains`) representing stations A and B.
Straightforward simulation of the scenario.
https://code.google.com/codejam/contest/32013/dashboard#s=p1&a=1
'''

def count_trains(trips, t):
    t = timedelta(minutes=t)
    num_trains = [0, 0]  # Trains starting from A and B
    trains = [[], []]  # The earliest available times for these trains
    for start, end, source in trips:
        # Check if earliest available train is earlier than the trip
        if trains[source] and trains[source][0] <= start:
            # Use this train
            heappop(trains[source])
        # Otherwise, create a new train
        else:
            num_trains[source] += 1
        # Now put the train back into the destination
        dest = 1 - source
        heappush(trains[dest], end+t)
    return " ".join(map(str, num_trains))


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        t = int(input())
        na, nb = [int(x) for x in input().split()]
        # trips will be [start, end, source], where source is 0 (A) or 1 (B)
        trips = []
        for _ in range(na):
            start, end = [datetime.strptime(x, "%H:%M")
                          for x in input().split()]
            trips.append([start, end, 0])
            # heappush(trips, [start, end, 0])
        for _ in range(nb):
            start, end = [datetime.strptime(x, "%H:%M")
                          for x in input().split()]
            trips.append([start, end, 1])
            # heappush(trips, [start, end, 0])
        print("Case #{}: {}".format(case, count_trains(sorted(trips), t)))


cases = int(input())  # read a line with a single integer
for c in range(1, cases + 1):
    f, s = [int(s) for s in input().split(" ")]
    maxes = [0] * s
    tickets = []
    for friend in range(f):
        a, b = [int(s) for s in input().split(" ")]
        if a == b:
            maxes[a-1] += 1
            continue
        if (a, b) in tickets:
            continue
        maxes[a-1] += 1
        maxes[b-1] += 1
        tickets.append((a, b))
    win = max(maxes)
    print("Case #{}: {}".format(c, win))

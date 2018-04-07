import sys
import math
import numpy as np

dug = np.array([[0] * 1000] * 1000)
 
def solve(width, row, col):
    global dug
    current_square = dug[row-1:row+2, col-1:col+2]
    # If 3s3 square has been filled, move
    if sum([sum(x) for x in current_square]) == 9:
        col += 1  # move onto next column
        if col > width:  # if the right edge of the rectangle has been reached
            col = 2  # reset column
            row += 1  # move onto next row
    # Keep digging at the same spot if the 3x3 square hasn't been filled
    coords = ' '.join([str(row), str(col)])
    print(coords)
    sys.stdout.flush()
    x, y = [int(x) for x in input().split()]
    if (x is y is 0) or (x is y is -1): 
        raise Exception("Gopher is ded")
    dug[x, y] = 1
    return row, col

cases = int(input())

for case in range(1, cases+1):
    a = int(input())  # minimum area
    height, width = 3, 3  # smallest area is 3x3 since gopher is *sigh*
    # Round area up to smallest rectangle
    while height * width < a:
        if height < width:
            height += 1
        else:
            width += 1
    row, col = 2, 2
    dug = np.array([[0] * 1001] * 1001)


    while True:
        try:
            row, col = solve(width, row, col)
        except:
            break

import sys
import math
# import numpy as np

def solve(width, row, col, dug):
    # current_square = dug[row-1:row+2, col-1:col+2]
    current_square = [dug[i][col-1:col+2] for i in range(row-1, row+2)]
    # If 3s3 square has been filled, move
    if sum([sum(x) for x in current_square]) == 9:
        col += 1  # move onto next column
        if col >= width:  # if the right edge of the rectangle has been reached
            col = 2  # reset column
            row += 1  # move onto next row
    # Keep digging at the same spot if the 3x3 square hasn't been filled
    coords = ' '.join([str(row), str(col)])
    print(coords)
    sys.stdout.flush()
    x, y = [int(x) for x in input().split()]
    if (x == y == 0) or (x == y == -1): 
        raise Exception("Gopher is ded")
    dug[x][y] = 1
    return row, col, dug

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
    dug=[[0 for x in range(1001)] for y in range(1001)]


    while True:
        try:
            row, col, dug = solve(width, row, col, dug)
        except:
            break

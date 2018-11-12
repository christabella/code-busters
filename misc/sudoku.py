''' Determine whether a partially-filled Sudoku board is solvable.

https://www.pramp.com/challenge/O5PGrqGEyKtq9wpgw6XP
'''

import numpy as np
N = 9


def get_candidates(board, i, j):
  '''Returns the possible values for cell (i, j) in a Sudoku grid.

  Args:
    board: (9x9 nparray) Sudoku grid
    i: (int) row of cell
    j: (int) column of cell
  Returns:
    a list of candidate values
  '''
  candidates = {str(i) for i in range(1, N + 1)}
  # Exclude all numbers already present in the same row, column, or subgrid.
  candidates -= set(board[i])
  candidates -= set(board[:, j])
  candidates -= set(board[3 * (i//3):3 * (i//3) + 3,
                          3 * (j//3):3 * (j//3) + 3].flatten())
  return candidates

def sudoku_solve(board):
  board = np.array(board)
  unfilled_coords = list(zip(*(np.where(board=='.'))))
  return solve(board, unfilled_coords, 0)


def solve(board, coords, ptr):
  '''Recursively check each successive unfilled cell

    Args:
      board: (np.array)

  '''
  # Positive base case where all cells have been filled
  if ptr == len(coords):
    return True
  i, j = coords[ptr]
  candidates = get_candidates(board, i, j)
  for c in candidates:
    # Write down tentative answer and try this branch
    board[i, j] = c
    has_future = solve(board, coords, ptr+1)
    if has_future:
      return True  # This branch has succeeded all the way
    # Implicit continue
  board[i, j] = '.'  # Welp, nothing worked so let's erase
  return False  # None of the future numbers worked out

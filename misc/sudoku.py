"""Determine whether a partially-filled Sudoku board is solvable.

https://www.pramp.com/challenge/O5PGrqGEyKtq9wpgw6XP
"""

import numpy as np
N = 9


def sudoku_solve(board):
  board = np.array(board)
  empty_coords = list(zip(*(np.where(board=='.'))))
  return solve(board, empty_coords, 0)

def solve(board, coords, ptr):
  """Recursively attempt to successively fill each empty cell

    Args:
      board: Numpy array of strings
      coords: List of (i, j) coordinates of empty cells in board
      ptr: The empty cell being explored

    Returns:
      A boolean indicating whether the cell was solvable
  """
  if ptr == len(coords):  # Positive base case where all cells are filled
    return True
  i, j = coords[ptr]
  candidates = get_candidates(board, i, j)
  for c in candidates:
    board[i, j] = c  # Write down tentative answer and try this branch
    if solve(board, coords, ptr+1):
      return True  # This branch has succeeded all the way
  board[i, j] = '.'  # Welp, nothing worked so let's erase
  return False  # None of the future numbers worked out

def get_candidates(board, i, j):
  """Returns the possible values for cell (i, j) in a Sudoku grid.

  Args:
    board: Numpy array of strings
    i: Row of cell
    j: Column of cell
  Returns:
    A list of candidate values
  """
  candidates = {str(i) for i in range(1, N + 1)}
  # Exclude all numbers already present in the same row, column, or subgrid.
  candidates -= set(board[i])
  candidates -= set(board[:, j])
  candidates -= set(board[3 * (i//3):3 * (i//3) + 3,
                          3 * (j//3):3 * (j//3) + 3].flatten())
  return candidates

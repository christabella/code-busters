'''https://res.cloudinary.com/practicaldev/image/fetch/s--3WTcSHjf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://upload.wikimedia.org/wikipedia/commons/8/8c/Sudoku_solved_by_bactracking.gif'''

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

candidates_dict = dict()
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
# g  print(ptr)
  if ptr == len(coords):
    return True
  i, j = coords[ptr]
  # We could actually cache the candidates for each (i, j)
  candidates = get_candidates(board, i, j)
#  print("for {}: {}".format((i, j), candidates))
  for c in candidates:
    # Write down tentative answer and try this branch
    board[i, j] = c
    has_future = solve(board, coords, ptr+1)
    if has_future:
      return True  # This branch has succeeded all the way
    board[i, j] = '.'  # Why is this critical? Because board is shared.
    # Otherwise (nothing worked out), try the next candidate
  return False  # None of the future numbers worked out

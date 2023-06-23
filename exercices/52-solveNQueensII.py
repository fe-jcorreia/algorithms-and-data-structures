def solveNQueens_old(n):
  board = [["."] * n for _ in range(n)]
  ans = 0

  def validPosition(i, j):
    for row in range(i):
      if board[row][j] == 'Q':
        return False

    for diag in range(n):
      if (i - diag >= 0) and (j - diag >= 0) and board[i - diag][j - diag] == 'Q':
        return False
    for diag in range(n):
      if (i - diag >= 0) and (j + diag < n) and board[i - diag][j + diag] == 'Q':
        return False

    return True

  def placeQueen(row):
    if row >= n:
      ans += 1
      return

    for j in range(n):
      if validPosition(row, j):
        board[row][j] = 'Q'
        placeQueen(row + 1)
        board[row][j] = '.'

  placeQueen(0)
  return ans


def solveNQueens(n):
  board = [["."] * n for _ in range(n)]
  ans = 0

  col = set()
  posDiag = set()
  negDiag = set()

  def placeQueen(row):
    nonlocal ans
    if row >= n:
      ans += 1
      return

    for j in range(n):
      if (j not in col) and (row + j not in posDiag) and (row - j not in negDiag):
        board[row][j] = 'Q'
        col.add(j)
        posDiag.add(row + j)
        negDiag.add(row - j)
        placeQueen(row + 1)
        board[row][j] = '.'
        col.remove(j)
        posDiag.remove(row + j)
        negDiag.remove(row - j)

  placeQueen(0)
  return ans


print(solveNQueens(1))
print(solveNQueens(4))

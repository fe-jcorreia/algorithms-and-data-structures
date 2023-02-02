def getPossibilities(board, i, j):
  possibilities = list(range(1,10))
  for line in range(9):
    if board[line][j] != '.' and int(board[line][j]) in possibilities:
      possibilities.remove(int(board[line][j]))

  for column in range(9):
    if board[i][column] != '.' and int(board[i][column]) in possibilities:
      possibilities.remove(int(board[i][column]))

  for line in range((i // 3) * 3, ((i // 3) * 3) + 3):
    for column in range((j // 3) * 3, ((j // 3) * 3) + 3):
      if board[line][column] != '.' and int(board[line][column]) in possibilities:
        possibilities.remove(int(board[line][column]))
  
  return possibilities

def isValid(board, i, j, char):
  for k in range(9):
    if board[i][k] == char:
      return False
    
    if board[k][j] == char:
      return False
    
    if board[((i // 3) * 3) + (k // 3)][((j // 3) * 3) + (k % 3)] == char:
      return False
    
  return True

def solve(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == '.':
        possibilities = getPossibilities(board, i, j)

        while possibilities:
          board[i][j] = str(possibilities.pop(0))
          if solve(board) == True:
            return True
          else:
            board[i][j] = '.'
        
        return False
  
  return True

def solveSudoku(board):
  solve(board)

def solve_opt(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == '.':
        for num in range(1,10):
          if isValid(board, i, j, str(num)):
            board[i][j] = str(num)

            if solve(board) == True:
              return True
            else:
              board[i][j] = '.'
        
        return False
  
  return True

def solveSudoku_opt(board):
  solve_opt(board)

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)

print("Solve O(27n²) time and O(n³) space")
for i in range(9):
  print(board[i])

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
solveSudoku_opt(board)

print("Optimized Solve O(9n²) time and O(n²) space")
for i in range(9):
  print(board[i])
    
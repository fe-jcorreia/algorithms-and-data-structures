def minPathSum(grid):
  m = len(grid)
  n = len(grid[0])
  matrix = [[float('inf')] * (n + 1) for _ in range(m + 1)]

  for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      if j == n - 1 and i == m - 1: 
        matrix[i][j] = grid[i][j]
        continue
      matrix[i][j] = grid[i][j] + min(matrix[i][j + 1], matrix[i + 1][j])
  
  return matrix[0][0]
    
print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))
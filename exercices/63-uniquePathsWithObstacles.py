def uniquePathsWithObstacles(obstacleGrid):
  m = len(obstacleGrid)
  n = len(obstacleGrid[0])
  matrix = [[0] * (n + 1) for _ in range(m + 1)]
  matrix[m - 1][n - 1] = 1
  matrix[m][n - 1] = 1

  for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      if obstacleGrid[i][j] == 1: matrix[i][j] = 0
      else: matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
    
  return matrix[0][0]

print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,1],[0,0]]))
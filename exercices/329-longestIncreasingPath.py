def dfs(matrix, lip, i, j, prev):
  m = len(matrix)
  n = len(matrix[0])
  
  if i < 0 or i == m or j < 0 or j == n or matrix[i][j] <= prev:
    return 0

  if lip.get((i, j)):
    return lip[(i, j)]
  
  maxLip = 1
  maxLip = max(maxLip, 1 + dfs(matrix, lip, i - 1, j, matrix[i][j])) # up
  maxLip = max(maxLip, 1 + dfs(matrix, lip, i, j + 1, matrix[i][j])) # right
  maxLip = max(maxLip, 1 + dfs(matrix, lip, i + 1, j, matrix[i][j])) # down
  maxLip = max(maxLip, 1 + dfs(matrix, lip, i, j - 1, matrix[i][j])) # left

  lip[(i, j)] = maxLip
  
  return maxLip


def longestIncreasingPath(matrix):
  m = len(matrix)
  n = len(matrix[0])
  lip = {}

  maxLip = 0
  for i in range(m):
    for j in range(n):
      maxLip = max(maxLip, dfs(matrix, lip, i, j, -1))
  
  return maxLip

print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(longestIncreasingPath([[1]]))
def maximalSquare(matrix):
  m = len(matrix)
  n = len(matrix[0])

  dp = [[0] * (n + 1) for _ in range(m + 1)]
  maxSize = 0

  for i in range(m - 1, -1 ,-1):
    for j in range(n - 1, -1, -1):
      if int(matrix[i][j]) == 1:
        if dp[i][j + 1] > 0 and dp[i + 1][j] > 0 and dp[i + 1][j + 1] > 0:
          dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        else:
          dp[i][j] = 1
        maxSize = max(maxSize, dp[i][j])

  return maxSize * maxSize

print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalSquare([["1","0","1","1","1"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalSquare([["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"]]))
print(maximalSquare([["0","1"],["1","0"]]))
print(maximalSquare([["0"]]))

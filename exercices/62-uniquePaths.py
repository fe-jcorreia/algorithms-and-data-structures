import math

def uniquePaths(m, n):
  matrix = [[0] * (n + 1) for _ in range(m + 1)]
  matrix[m - 1][n - 1] = 1
  matrix[m][n - 1] = 1

  for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]

  return matrix[0][0]

def uniquePaths(m, n):
  return int(math.factorial(m + n - 2) / (math.factorial(m-1) * math.factorial(n-1)))

print(uniquePaths(3, 2))
print(uniquePaths(3, 7))

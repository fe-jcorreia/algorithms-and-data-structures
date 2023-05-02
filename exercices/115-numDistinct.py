def numDistinct_old(s, t):
  m = len(t)
  cache = {}

  def dfs(i, j):
    if (i, j) in cache: return cache[(i, j)]
    if j >= m: return 1

    total = 0
    n = len(s[i:])
    for k in range(n):
      if s[i:][k] == t[j]:
        total += dfs(i + k + 1, j + 1)

    cache[(i, j)] = total
    return total

  return dfs(0, 0)

def numDistinct_old2(s, t):
  m, n = len(s), len(t)
  cache = {}

  def dfs(i, j):
    if (i, j) in cache: return cache[(i, j)]
    if j >= n: return 1
    if i >= m: return 0

    total = 0
    if s[i] == t[j]:
      total += dfs(i + 1, j + 1)
    total += dfs(i + 1, j)

    cache[(i, j)] = total
    return total

  return dfs(0, 0)

def numDistinct(s, t):
  m, n = len(s), len(t)
  dp = [[0] * (n + 1) for _ in range(m + 1)]
  for k in range(m + 1): dp[k][0] = 1

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      dp[i][j] = dp[i - 1][j]
      if s[i - 1] == t[j - 1]:
        dp[i][j] += dp[i - 1][j - 1]

  return dp[m][n]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))

def minDistance_old(word1, word2):
  n, m = len(word1), len(word2)

  cache = {}
  def dfs(i, j):
    if (i, j) in cache: return cache[(i ,j)]
    if i >= n and j >= m: return 0
    if i < n and j >= m: return n - i
    if j < m and i >= n: return m - j

    minOp = float('inf')
    if word1[i] == word2[j]:
      minOp = min(minOp, dfs(i + 1, j + 1))
    else:
      minOp = min(minOp, 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)))
    
    cache[(i, j)] = minOp
    return cache[(i, j)]

  return dfs(0, 0)

def minDistance(word1, word2):
  n, m = len(word1), len(word2)

  dp = [[0] * (n + 1) for _ in range(m + 1)]
  for i in range(n + 1):
    dp[0][i] = i
  for j in range(m + 1):
    dp[j][0] = j

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if word1[j - 1] == word2[i - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

  return dp[m][n]

print(minDistance("horse", "ros"))
print(minDistance("intention", "execution"))
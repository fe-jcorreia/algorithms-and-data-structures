def isMatch_old(s, p):
  m, n = len(s), len(p)
  cache = {}

  def dfs(i, j):
    if (i, j) in cache: return cache[(i,j)]

    if i >= m and j >= n: return True
    if j >= n: return False

    match = i < m and (s[i] == p[j] or p[j] == '.') 
    if (j + 1) < n and p[j + 1] == "*":
      cache[(i,j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
      return cache[(i,j)]

    if match:
      cache[(i,j)] = dfs(i + 1, j + 1)
      return cache[(i,j)]

    return False

  return dfs(0,0)

def isMatch(s, p):
  n, m = len(s), len(p)
  dp = [[False] * (m + 1) for _ in range(n + 1)]
  dp[0][0] = True
  
  for i in range(n + 1):
    for j in range(1, m + 1):
      if p[j - 1] == "*":
        dp[i][j] = dp[i][j - 2] or (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[i - 1][j])
      else:
        dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
  
  return dp[n][m]

print(isMatch("aa", "a")) # false
print(isMatch("aa", "a*")) # true
print(isMatch("ab", ".*")) # true
print(isMatch("aab", "c*a*b")) # true
print(isMatch("ab", ".*c")) # false
print(isMatch("mississipi", "mis*is*p*.")) # false
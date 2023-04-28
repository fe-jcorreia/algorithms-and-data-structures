def isMatch(s, p):
    i = 0
    j = 0
    match = 0
    star = -1
    while i < len(s):
      if j < len(p) and (s[i] == p[j] or p[j] == '?'):
        i += 1
        j += 1
      elif j < len(p) and p[j] == '*':
        match = i
        star = j
        j += 1
      elif (star != -1):
        j = star + 1
        match = match + 1
        i = match
      else:
        return False
    
    while j < len(p) and p[j] == '*':
      j = j + 1
        
    if j == len(p):
      return True
    else:
      return False

def isMatch_old(s, p):
  n, m = len(s), len(p)
  dp = [[False] * (m + 1) for _ in range(n + 1)]
  dp[0][0] = True

  for i in range(n + 1):
    for j in range(1, m + 1):
      if p[j - 1] == '*':
        dp[i][j] = dp[i][j - 1] or (i > 0 and dp[i - 1][j])
      else:
        dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "?")
  
  return dp[n][m]



print(isMatch("aa", "a")) # false
print("-----------------------------------------")
print(isMatch("aa", "*")) # true
print("-----------------------------------------")
print(isMatch("ab", "?*")) # true
print("-----------------------------------------")
print(isMatch("aab", "**b")) # true
print("-----------------------------------------")
print(isMatch("ab", "?*c")) # false
print("-----------------------------------------")
print(isMatch("mississipi", "mi*i*p*?")) # false
def isScramble(s1, s2):
  cache = {}
  def dfs(s, u):
    if (s, u) in cache: return cache[(s, u)]
    if s == u: return True

    n = len(s)
    for i in range(1, n):    
      if (dfs(s[:i], u[:i]) and dfs(s[i:], u[i:])) or (dfs(s[:i], u[n - i:]) and dfs(s[i:], u[:n - i])): 
        cache[(s, u)] = True
        return True
    
    cache[(s, u)] = False
    return False
  
  return dfs(s1, s2)

def isScramble(s1, s2):
  cache = {}
  def dfs(a, b):
    if (a,b) in cache: return cache[(a,b)]
    if a == b:
      return True

    if Counter(a) != Counter(b):
      cache[(a,b)] = False
      return False

    checkSub = any(
      dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]) or \
      dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i])
      for i in range(1, len(a))
    )

    cache[(a,b)] = checkSub
    return checkSub
  
  return dfs(s1, s2)

print(isScramble("great", "rgeat"))
print(isScramble("abcde", "caebd"))
print(isScramble("a", "a"))
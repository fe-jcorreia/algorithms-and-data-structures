def partition(s):
  res = []
  curPar = []

  def isPal(u):
    l = 0
    r = len(u) - 1 
    while l < r:
      if u[l] != u[r]:
        return False
      l, r = l + 1, r - 1
    return True
  
  def dfs(i):
    if i >= len(s):
      res.append(curPar.copy())
      return 
    for j in range(i, len(s)):
      if isPal(s[i:j + 1]):
        curPar.append(s[i:j + 1])
        dfs(j + 1)
        curPar.pop()
        
  dfs(0)
  return res

print(partition("aab"))
print(partition("a"))
print(partition("aaab"))
print(partition("abcaa"))
print(partition("abbab"))
print(partition("abaca"))
print(partition("aaa"))

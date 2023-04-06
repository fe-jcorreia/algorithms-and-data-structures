def isSubsequence(s, t):
  n = len(s)
  m = len(t)
  if n > m: return False
  if n == 0: return True
  
  i = 0
  nextChar = s[i]

  for char in t:
    if char == nextChar:
      i += 1
      if i == n: return True
      nextChar = s[i]

  return False

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
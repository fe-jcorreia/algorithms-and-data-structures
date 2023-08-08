def repeatedSubstringPattern_old(s):
  sFold = s[1:] + s[:-1]
  n = len(sFold)
  m = len(s)

  for i in range(n - m + 1):
    for j in range(m):
      if sFold[i + j] != s[j]: break
      if j == m - 1: return True

  return False

def repeatedSubstringPattern_old2(s):
  return s in s[1:] + s[:-1]

def repeatedSubstringPattern(s):
  sFold = s[1:] + s[:-1]
  n = len(sFold)
  m = len(s)

  lps = [0] * m
  prevLPS, i = 0, 1

  while i < m:
    if s[i] == s[prevLPS]:
      lps[i] = prevLPS + 1
      prevLPS += 1
      i += 1
    elif prevLPS == 0:
      lps[i] = 0
      i += 1
    else:
      prevLPS = lps[prevLPS - 1]
  
  i = j = 0
  while i < n:
    if sFold[i] == s[j]:
      i, j = i + 1, j + 1
    else:
      if j == 0:
        i += 1
      else:
        j = lps[j - 1]

    if j == m:
      return True
    
  return False

print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))
def rotateString_old(s, goal):
  if len(s) != len(goal): return False
  
  haystack = goal + goal

  m = len(s)
  n = len(haystack)
  lps = [0] * m

  prev, i = 0, 1
  while i < m:
    if s[i] == s[prev]:
      lps[i] = prev + 1
      prev += 1
      i += 1
    elif prev == 0:
      lps[i] = 0
      i += 1
    else:
      prev = lps[prev - 1]
  
  i = j = 0
  while i < n:
    if haystack[i] == s[j]:
      i, j = i + 1, j + 1
    else:
      if j == 0: i += 1
      else: j = lps[j - 1]
    
    if j == m:
      return True
    
  return False

def rotateString(s, goal):
  if len(s) != len(goal): return False
  haystack = goal + goal
  
  if s in haystack: return True
  return False
 
print(rotateString("abcde", "cdeab"))
print(rotateString("abcde", "abced"))
print(rotateString("bbbacddceeb", "ceebbbbacdd"))

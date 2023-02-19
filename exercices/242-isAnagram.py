def isAnagram(s, t):
  if len(s) != len(t):
    return False
  
  seen = {}

  for char in s:
    seen[char] = 1 + seen.get(char, 0)

  for char in t:
    if seen.get(char, 0) == 0:
      return False
    
    seen[char] -= 1
  
  return True

def isAnagram2(s, t):
  return sorted(s) == sorted(t)
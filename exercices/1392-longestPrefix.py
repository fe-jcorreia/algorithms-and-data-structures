def longestPrefix(s):
  m = len(s)
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

  return s[:lps[-1]] 

print(longestPrefix("level"))
print(longestPrefix("ababab"))
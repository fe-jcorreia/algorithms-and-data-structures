def shortestPalindrome_old(s):
  m = len(s)
  reverse = s[::-1]
  prefix = []

  for i in range(m):
    a = s[:m - i] 
    if a != reverse[i:]:
      prefix.append(a[-1])
    else:
      break

  return "".join(prefix) + s

def shortestPalindrome(s):
  sAndReverse = s + '#' + s[::-1]
  
  m = len(sAndReverse)
  lps = [0] * m
  prev, i = 0, 1
  while i < m:
    if sAndReverse[i] == sAndReverse[prev]:
      lps[i] = prev + 1
      prev += 1
      i += 1
    elif prev == 0:
      lps[i] = 0
      i += 1
    else:
      prev = lps[prev - 1]

  palindromicPart = lps[-1]
  prefix = s[palindromicPart:][::-1]

  return prefix + s

print(shortestPalindrome("ababc"))
print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abcd"))
print(shortestPalindrome("aabba"))
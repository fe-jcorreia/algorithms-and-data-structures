def strStr_bruteForce(haystack, needle):
  n = len(needle)
  m = len(haystack)

  if n > m: return -1

  for i in range(m):
    for j in range(n):
      if i + j >= m or haystack[i + j] != needle[j]:
        break
      if j == n - 1: return i
  
  return -1

def strStr_KMP(haystack, needle):
  if needle == "": return 0
  n = len(haystack)
  m = len(needle)

  lps = [0] * m
  prevLPS, i = 0, 1

  while i < m:
    if needle[i] == needle[prevLPS]:
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
    if haystack[i] == needle[j]:
      i, j = i + 1, j + 1
    else:
      if j == 0:
        i += 1
      else:
        j = lps[j - 1]
     
    if j == m:
      return i - m
  
  return -1

def strStr(haystack, needle):
  m = len(needle)
  n = len(haystack)

  badChar = [-1] * 256

  for i in range(m):
    badChar[ord(needle[i])] = i
  
  s = 0
  while(s <= n - m):
    j = m - 1

    while j >= 0 and needle[j] == haystack[s + j]:
      j -= 1

    if j < 0:
      return s 
      # s += (m - badChar[ord(haystack[s + m])] if s + m < n else 1)
    else:
      s += max(1, j - badChar[ord(haystack[s + j])])
  
  return -1
  
  
 

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("mississippi", "issipi"))
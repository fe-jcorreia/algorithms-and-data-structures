def search(haystack, needle):
  m = len(needle)
  n = len(haystack)

  badChar = [-1] * 256

  for i in range(m):
    badChar[ord(needle[i])] = i
  
  print(badChar)
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

print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("sadbutsad", "sad"))
print(search("leetcode", "leeto"))
print(search("mississippi", "issipi"))
def search(haystack, needle):
  m = len(needle)
  n = len(haystack)
  d = 256
  q = 101
  hNeedle = 0
  hHaystack = 0
  h = (d**(m - 1)) % q
 
  for i in range(m):
    hNeedle = (d * hNeedle + ord(needle[i])) % q
    hHaystack = (d * hHaystack + ord(haystack[i])) % q

  j = 0
  for i in range(n - m + 1):
    if hNeedle == hHaystack:
      for j in range(m):
        if haystack[i + j] != needle[j]:
          break
      if j == m - 1: return i

    if i < n - m:
      hHaystack = (d * (hHaystack - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
      if hHaystack < 0: hHaystack += q
  
  return -1
 
    
 

print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("sadbutsad", "sad"))
print(search("leetcode", "leeto"))
print(search("mississippi", "issipi"))
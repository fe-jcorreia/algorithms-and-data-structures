def search(haystack, needle):
  n = len(needle)
  m = len(haystack)

  if n > m: return -1

  for i in range(m):
    for j in range(n):
      if i + j >= m or haystack[i + j] != needle[j]:
        break
      if j == n - 1: return i
  
  return -1

print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("sadbutsad", "sad"))
print(search("leetcode", "leeto"))
print(search("mississippi", "issipi"))
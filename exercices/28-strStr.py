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

def strStr(haystack, needle):
  pass
    

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("mississippi", "issipi"))
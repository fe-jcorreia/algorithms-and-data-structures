def longestPalindrome(s):
  maxPal = ""
  n = len(s)

  for i in range(n):
    l, r = i, i
    while l >= 0 and s[l] == s[i]: l -= 1
    while r < n and s[r] == s[i]: r += 1

    pal = s[l + 1:r]
    while l >= 0 and r < n and s[l] == s[r]:
      pal = s[l:r + 1]
      l -= 1
      r += 1

    maxPal = max(maxPal, pal, key=len)
  
  return maxPal

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("abcdexbabxabc"))
print(longestPalindrome("abcdexbaabxabc"))

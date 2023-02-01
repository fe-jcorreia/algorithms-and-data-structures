def lengthOfLongestSubstring(s):
  if len(s) == 0:
    return 0

  seen = {}
  maxLen = 0
  start = 0
  end = 0

  for i, char in enumerate(s):
    if char in seen and seen[char] >= start:
      maxLen = max(maxLen, end - start + 1)
      start = seen[char] + 1
    
    seen[char] = i
    end = i
  
  return max(maxLen, end - start + 1)


print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring(" ")) # 1
print(lengthOfLongestSubstring("aa")) # 1
print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("pwwkew")) # 3
print(lengthOfLongestSubstring("dvdf")) # 3
print(lengthOfLongestSubstring("tmmzuxt")) # 5
print(lengthOfLongestSubstring("ckilbkda")) # 6
print(lengthOfLongestSubstring("123456789tmmzuxt")) # 11
print(lengthOfLongestSubstring(" rjweaps30df pss")) # 12
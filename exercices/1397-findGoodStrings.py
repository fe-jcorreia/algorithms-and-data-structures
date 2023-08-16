from functools import lru_cache

def findGoodStrings(n, s1, s2, evil):  
  @lru_cache(None)
  def dp(index, isS1Prefix, isS2Prefix, matchedEvilLength):
    if matchedEvilLength == m:
      return 0
    if index == n:
      return 1
    
    start = ord(s1[index]) if isS1Prefix else ord('a')
    end = ord(s2[index]) if isS2Prefix else ord('z')

    ans = 0
    for i in range(start, end + 1):
      currChar = chr(i)
      tmpLen = matchedEvilLength
      while tmpLen > 0 and currChar != evil[tmpLen]:
        tmpLen = lps[tmpLen - 1]
      
      if currChar == evil[tmpLen]:
        tmpLen += 1

      ans += dp(index + 1, isS1Prefix and i == start, isS2Prefix and i == end, tmpLen)
    
    return ans
  
  m = len(evil)
  lps = [0] * m
  j = 0
  for i in range(1, m):
    while j > 0 and evil[i] != evil[j]:
      j = lps[j - 1]
    if evil[i] == evil[j]:
      lps[i] = j + 1
      j += 1
    
  mod = 1_000_000_007
  return dp(0, True, True, 0) % mod

print(findGoodStrings(2,"aa","da","b")) # 51
print(findGoodStrings(8,"leetcode","leetgoes","leet")) # 0
print(findGoodStrings(2,"gx","gz","x")) # 2

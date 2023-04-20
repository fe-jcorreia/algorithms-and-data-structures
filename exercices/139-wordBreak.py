def wordBreak(s, wordDict):
  n = len(s)

  dp = [False] * (n + 1)
  dp[n] = True
  for i in range(n - 1, -1 ,-1):
    for word in wordDict:
      if (i + len(word)) <= n and s[i: i + len(word)] == word:
        dp[i] = dp[i + len(word)]
      if dp[i]: break

  return dp[0]



print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreak("a", ["b"]))
print(wordBreak("bb", ["a","b","bbb","bbbb"]))
print(wordBreak("cars", ["car","ca","rs"]))
print(wordBreak("aaaaaaa", ["aaaa","aaa"]))
print(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
                ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
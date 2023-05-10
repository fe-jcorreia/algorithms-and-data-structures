def wordBreak(s, wordDict):
  wordSet = set(wordDict)
  n = len(s)
  currSentence = []
  sentences = []

  def dfs(i):
    if i >= n:
      sentences.append(" ".join(currSentence))
      return

    for j in range(i, n):
      string = s[i: j + 1]
      if string in wordSet:
        currSentence.append(string)
        dfs(j + 1)
        currSentence.pop()
      
  dfs(0)
  return sentences

print(wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreak("aaaaaaaaaaaaaaaaaaab", 
                ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
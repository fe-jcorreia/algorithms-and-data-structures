def combinationSum(candidates, target):
  ans = []
  currCandidates = []
  currSum = 0
  n = len(candidates)

  def buildCandidates(index):
    nonlocal currSum

    if currSum == target:
      ans.append(currCandidates.copy())
      return
    
    for i in range(index, n):
      if candidates[i] + currSum <= target:
        currSum += candidates[i]
        currCandidates.append(candidates[i])
        buildCandidates(i)
        currSum -= candidates[i]
        currCandidates.pop()

  buildCandidates(0)
  return ans

def combinationSum_dp(candidates, target):
  dp = [[] for _ in range(target + 1)]
  for c in candidates:
    for i in range(c, target + 1):
      if i == c: dp[i].append([c])
      for comb in dp[i - c]: dp[i].append(comb + [c])
  
  return dp[-1]

def combinationSum_neetcode(candidates, target):
  res = []

  def dfs(i, cur, total):
    if total == target:
      res.append(cur.copy())
      return
    if i >= len(candidates) or total > target:
      return
    
    cur.append(candidates[i])
    dfs(i, cur, total + candidates[i])
    cur.pop()
    dfs(i + 1, cur, total)

  dfs(0, [], 0)
  return res


print(combinationSum([2,3,6,7], 7))
# print(combinationSum([2,3,5], 8))
# print(combinationSum([2], 1))
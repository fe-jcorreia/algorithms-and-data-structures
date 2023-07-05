def combinationSum2(candidates, target):
  candidates = sorted(candidates)
  ans = []
  currCandidates = []
  currSum = 0
  seen = set()
  n = len(candidates)

  def buildCandidates(index):
    nonlocal currSum
    if currSum == target:
      if tuple(currCandidates) not in seen:
        ans.append(currCandidates.copy())
        seen.add(tuple(currCandidates))
      return
    
    prev = -1
    for i in range(index, n):
      if candidates[i] == prev:
        continue
      if candidates[i] + currSum <= target:
        currSum += candidates[i]
        currCandidates.append(candidates[i])
        buildCandidates(i + 1)
        currSum -= candidates[i]
        currCandidates.pop()
        prev = candidates[i]
  
  buildCandidates(0)
  return ans

def combinationSum2_(candidates, target):
  candidates.sort()
  res = []

  def backtrack(cur, pos, target):
    if target == 0:
      res.append(cur.copy())
    if target <= 0:
      return
  
    prev = -1
    for i in range(pos, len(candidates)):
      if candidates[i] == prev:
        continue
      cur.append(candidates[i])
      backtrack(cur, i + 1, target - candidates[i])
      cur.pop()

      prev = candidates[i]

  backtrack([], 0, target)
  return res


print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))

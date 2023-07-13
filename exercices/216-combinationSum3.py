def combinationSum3(k, n):
  ans = []
  currComb = []

  def dfs(index, currSum):
    if len(currComb) == k:
      if currSum == n:
        ans.append(currComb[:])
      return

    for i in range(index, 10):
      if currSum + i <= n:
        currComb.append(i)
        dfs(i + 1, currSum + i)
        currComb.pop()
  
  dfs(1, 0)
  return ans


print(combinationSum3(3,7))
print(combinationSum3(3,9))
print(combinationSum3(4,1))
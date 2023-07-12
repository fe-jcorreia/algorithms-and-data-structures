def subsetsWithDup(nums):
  nums = sorted(nums)
  seen = set()
  ans = []
  currSub = []

  def dfs(index):
    if tuple(currSub) not in seen:
      seen.add(tuple(currSub))
      ans.append(currSub[:])
    
    prev = float("-inf")
    for i in range(index, len(nums)):
      if prev != nums[i]:
        currSub.append(nums[i])
        dfs(i + 1)
        currSub.pop()
        prev = nums[i]

  dfs(0)
  return ans

print(subsetsWithDup([1,2,2]))
print(subsetsWithDup([0]))
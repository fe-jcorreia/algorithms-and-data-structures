def permuteUnique(nums):
  ans = []
  currPerm = []
  used = {}

  for num in nums:
    used[num] = 1 + used.get(num, 0)

  def dfs():
    if len(currPerm) == len(nums):
      ans.append(currPerm[:])
      return

    for i in used:
      if used[i] > 0:
        used[i] -= 1
        currPerm.append(i)
        dfs()
        used[i] += 1
        currPerm.pop()

  dfs()
  return ans

# print(permuteUnique([1,1,2]))
# print(permuteUnique([1,2,3]))
print(permuteUnique([3,3,0,3]))
def subsets(nums):
  seen = set()
  ans = []
  currSub = []

  def dfs(index):
    if tuple(currSub) not in seen:
      seen.add(tuple(currSub))
      ans.append(currSub[:])
    
    for i in range(index, len(nums)):
      currSub.append(nums[i])
      dfs(i + 1)
      currSub.pop()

  dfs(0)
  return ans

def subsets_(nums):
  ans = []
  currSub = []

  def dfs(index):
    if index >= len(nums):
      ans.append(currSub[:])
      return

    currSub.append(nums[index])
    dfs(index + 1)
    currSub.pop()
    dfs(index + 1)

  dfs(0)
  return ans


print(subsets([1,2,3]))
print(subsets([0]))

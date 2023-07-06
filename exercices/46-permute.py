def permute(nums):
  ans = []
  currPerm = []
  used = set()
  n = len(nums)

  def dfs():
    if len(currPerm) == n:
      ans.append(currPerm.copy()) 
      return
  
    for item in nums:
      if item not in used:
        currPerm.append(item)
        used.add(item)
        dfs()
        currPerm.pop()
        used.remove(item)
    
  dfs()
  return ans

def permute_(nums):
  result = []

  if len(nums) == 1:
    return [nums[:]]
  
  for _ in range(len(nums)):
    n = nums.pop(0)
    perms = permute(nums)

    for perm in perms:
      perm.append(n)
    result.extend(perms)
    nums.append(n)

  return result

print(permute([1,2,3]))
print(permute([0,1]))
print(permute([1]))
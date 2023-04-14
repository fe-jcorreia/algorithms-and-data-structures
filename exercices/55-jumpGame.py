def canJump_old(nums):
  n = len(nums)
  jumps = [False] * (n - 1)

  for i in range(n - 2, -1, -1):
    if nums[i] + i >= n - 1:
      jumps[i] = True
    else:
      for j in range(1, nums[i]):
        if jumps[i + j] == True:
          jumps[i] = True
          break
  
  return jumps[0]

def canJump(nums):
  n = len(nums)
  l, r = 0, 0

  while r < n - 1:
    maxJump = 0
    for i in range(l, r + 1):
      maxJump = max(maxJump, i + nums[i])
    if maxJump == 0: return False
    l = r + 1
    r = maxJump
  
  return True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))

def jump_old(nums):
  n = len(nums)
  if n == 1: return 0
  jumps = [float('inf')] * (n - 1)

  for i in range(n - 2, -1, -1):
    if nums[i] == 0: continue
    
    if nums[i] >= (n - 1) - i:
      jumps[i] = 1
    else:
      jumps[i] = 1 + min(jumps[i + 1:i + nums[i] + 1])
  
  return jumps[0]

def jump(nums):
  n = len(nums)
  res = 0
  l = r = 0

  while r < n - 1:
    maxJump = 0
    for i in range(l, r + 1):
      maxJump = max(maxJump, i + nums[i])
    l = r + 1
    r = maxJump
    res += 1
  
  return res


print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))
print(jump([1,1,1,1]))
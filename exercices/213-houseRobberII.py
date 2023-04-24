def rob(nums):
  n = len(nums)
  if n == 1: return nums[0]
  
  last, twoLast = 0, 0
  for i in range(1, n):
    curr = max(twoLast + nums[i], last)
    twoLast = last
    last = curr

  skipFirst = last

  last, twoLast = 0, 0
  for i in range(n - 1):
    curr = max(twoLast + nums[i], last)
    twoLast = last
    last = curr

  skipLast = last

  return max(skipFirst, skipLast)

print(rob([2,3,2])) # 3
print(rob([1,2,3,1])) # 4
print(rob([1,2,3])) # 3
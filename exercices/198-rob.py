def rob(nums):
  n = len(nums)
  last, twoLast = 0, 0

  for i in range(n - 1, -1, -1):
    curr = max(twoLast + nums[i], last)
    twoLast = last
    last = curr

  return last

print(rob([1,2,3,1])) # 4
print(rob([2,7,9,3,1])) # 12
print(rob([8,2,7,9,3,1])) # 18
print(rob([2,1,1,2])) # 4

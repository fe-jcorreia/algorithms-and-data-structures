def maxProduct(nums):
  res = max(nums)
  curMin, curMax = 1, 1

  for n in nums:
    if n == 0:
      curMax, curMin = 1, 1
      continue

    tmp = n * curMax
    curMax = max(tmp, n * curMin, n)
    curMin = min(tmp, n * curMin, n)
    res = max(res, curMax, curMin)

  return res

print(maxProduct([2,3,-2,4])) # 6
print(maxProduct([2,3,-2,-4])) # 48
print(maxProduct([-5,2,3,-2,-4])) # 60
print(maxProduct([2,3,-2,-4,-5])) # 48
print(maxProduct([-2,0,-1])) # 0
print(maxProduct([-2,0,5])) # 5
print(maxProduct([-2,2,-1])) # 4
print(maxProduct([0,2])) # 2
print(maxProduct([3,-1,4])) # 4
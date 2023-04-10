def getMaximumGenerated(n):
  nums = [0, 1]
  if n == 0: return 0

  for i in range(2, n + 1):
    if i % 2 == 0:
      nums.append(nums[i // 2])
    else:
      nums.append(nums[i // 2] + nums[(i // 2) + 1])
  
  return max(nums)

print('n = 0:', getMaximumGenerated(0))
print('n = 1:', getMaximumGenerated(1))
print('n = 2:', getMaximumGenerated(2))
print('n = 3:', getMaximumGenerated(3))
print('n = 4:', getMaximumGenerated(4))
print('n = 5:', getMaximumGenerated(5))
print('n = 6:', getMaximumGenerated(6))
print('n = 7:', getMaximumGenerated(7))
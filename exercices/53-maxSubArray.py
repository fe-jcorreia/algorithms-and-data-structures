def maxSubArray_old(nums):
  maxSum = sumBefore = nums[0]

  for i in range(1, len(nums)):
    maxSum = max(maxSum, nums[i] + sumBefore, nums[i])
    if nums[i] + sumBefore > nums[i]:
      sumBefore = nums[i] + sumBefore
    else:
      sumBefore = nums[i]

  return maxSum

def maxSubArray(nums):
  maxSum = sumBefore = nums[0]

  for i in range(1, len(nums)):
    if sumBefore < 0: sumBefore = 0
    sumBefore += nums[i]
    maxSum = max(maxSum, sumBefore)

  return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
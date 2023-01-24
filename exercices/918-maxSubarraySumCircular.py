from sys import maxsize

def maxSubarraySumCircular(nums):
  maxSum = -maxsize - 1
  n = len(nums)
  
  for k in range(1,len(nums) + 1):
    for i in range(len(nums)):
      currentMaxSum = nums[i]
      for j in range(i + 1, i + k):
        currentMaxSum += nums[j % n]
      maxSum = max(maxSum, currentMaxSum)

  return maxSum

def maxSubarraySumCircular_opt(nums):
  maxSum = nums[0]
  minSum = nums[0]
  currentMaxSum = 0
  currentMinSum = 0
  totalSum = 0

  for num in nums:
    currentMaxSum = max(currentMaxSum + num, num)
    maxSum = max(maxSum, currentMaxSum)
    currentMinSum = min(currentMinSum + num, num)
    minSum = min(minSum, currentMinSum)
    totalSum += num
        
  return maxSum if minSum == totalSum else max(maxSum, totalSum - minSum)


print(maxSubarraySumCircular([1,-2,3,-2])) # 3
print(maxSubarraySumCircular([-3,-2,-3])) # -2
print(maxSubarraySumCircular([-5,4,-6])) # 4
print(maxSubarraySumCircular([5,-3,5])) # 10
print(maxSubarraySumCircular([-2,4,-5,4,-5,9,4])) # 15

print(maxSubarraySumCircular_opt([1,-2,3,-2])) # 3
print(maxSubarraySumCircular_opt([-3,-2,-3])) # -2
print(maxSubarraySumCircular_opt([-5,4,-6])) # 4
print(maxSubarraySumCircular_opt([5,-3,5])) # 10
print(maxSubarraySumCircular_opt([-2,4,-5,4,-5,9,4])) # 15
print(maxSubarraySumCircular_opt([1,2,3])) # 6

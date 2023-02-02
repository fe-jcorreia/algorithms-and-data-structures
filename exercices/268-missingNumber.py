def missingNumber(nums):
  for i in range(len(nums) + 1):
    if i not in nums:
      return i

def missingNumber_opt(nums):
  sumNums = 0
  totalSum = 0

  for i in range(len(nums)):
    sumNums += nums[i]
    totalSum += i + 1

  return totalSum - sumNums    

print(missingNumber([3,0,1])) # 2
print(missingNumber([0,1])) # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8

print("missingNumber optmization:")
print(missingNumber_opt([3,0,1])) # 2
print(missingNumber_opt([0,1])) # 2
print(missingNumber_opt([9,6,4,2,3,5,7,0,1])) # 8

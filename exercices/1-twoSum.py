# time: O(n^2) space: O(n^2)
def twoSum(nums, target):
  for i, first in enumerate(nums):
    for j, second in enumerate(nums[i + 1:]):
      if first + second == target:
        return [i, i + 1 + j]

# time: O(n) space: O(n)
def twoSum_opt(nums, target):
  seen = {}
  for i, number in enumerate(nums):
    complement = target - number

    if complement in seen:
      return [seen[complement], i]
    
    seen[number] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

print(twoSum_opt([2,7,11,15], 9))
print(twoSum_opt([3,2,4], 6))
print(twoSum_opt([3,3], 6))
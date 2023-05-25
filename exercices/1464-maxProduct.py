import heapq

def maxProduct(nums):
  i = max(0, 1, key=lambda x: nums[x])
  j = 0 if i != 0 else 1

  for k in range(2, len(nums)):
    if nums[k] > nums[i]:
      j = i
      i = k
    if nums[k] > nums[j] and k != i:
      j = k
  
  return (nums[i] - 1) * (nums[j] - 1)

print(maxProduct([3,4,5,2]))
print(maxProduct([1,5,4,5]))
print(maxProduct([3,7]))
print(maxProduct([10,2,5,2]))

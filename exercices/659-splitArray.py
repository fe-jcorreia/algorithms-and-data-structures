def isPossible(nums):
  if len(nums) < 3: return False

  frequency = {}
  for num in nums: frequency[num] = 1 + frequency.get(num, 0)
  subsequence = {}

  for num in nums:
    if frequency[num] == 0:
      continue
    frequency[num] -= 1
    
    if subsequence.get(num - 1, 0) > 0:
      subsequence[num - 1] -= 1
      subsequence[num] = subsequence.get(num, 0) + 1
    elif frequency.get(num + 1, 0) and frequency.get(num + 2, 0):
      frequency[num + 1] -= 1
      frequency[num + 2] -= 1
      subsequence[num + 2] = subsequence.get(num + 2, 0) + 1
    else:
      return False
    
  return True
     


print(isPossible([1,2,3,3,4,5]))
print(isPossible([1,2,3,3,4,4,5,5]))
print(isPossible([1,2,3,4,4,5]))
print(isPossible([1,2,3]))

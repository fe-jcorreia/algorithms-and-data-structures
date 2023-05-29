def minimumOperations(nums):
  numSet = set(nums)
  
  if 0 in numSet: return len(numSet) - 1
  else: return len(numSet)


print(minimumOperations([1,5,0,3,5]))
print(minimumOperations([0]))

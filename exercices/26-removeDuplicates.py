def removeDuplicates(nums):
  currIndex = 0
  for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]: continue
    currIndex += 1
    nums[currIndex] = nums[i]
  
  return currIndex + 1

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
def removeElement(nums, val):
  currIndex = 0
  for i in range(len(nums)):
    if nums[i] == val: continue
    nums[currIndex] = nums[i]
    currIndex += 1
  
  return currIndex

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))

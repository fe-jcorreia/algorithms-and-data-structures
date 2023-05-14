def moveZeroes(nums):
  zeroCount = 0
  currPos = 0
  for i in range(len(nums)):
    if nums[i] == 0: zeroCount += 1
    else:
      nums[currPos] = nums[i]
      currPos += 1

  for i in range(zeroCount):
    nums[-1 - i] = 0

  return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))

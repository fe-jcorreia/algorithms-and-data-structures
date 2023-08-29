def singleNumber(nums):
  ones, twos = 0, 0

  for num in nums:
    ones ^= (num & ~twos)
    twos ^= (num & ~ones)

  return ones

print(singleNumber([2,2,3,2]))
print(singleNumber([0,1,0,1,0,1,99]))

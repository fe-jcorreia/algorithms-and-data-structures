def singleNumber(nums):
  seen = set()
  for num in nums:
    if num in seen: seen.remove(num)
    else: seen.add(num)
    
  return list(seen)[0]

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))
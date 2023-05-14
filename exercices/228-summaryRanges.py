def summaryRanges(nums):
  ans = []
  if not nums: return ans
  
  start, curr = nums[0], nums[0]
  for i in range(1, len(nums)):
    if nums[i] == curr + 1:
      curr += 1
    else:
      if start == curr: ans.append(str(start))
      else: ans.append(f"{start}->{curr}")
      start, curr = nums[i], nums[i]
  
  if start == curr: ans.append(str(start))
  else: ans.append(f"{start}->{curr}")
  
  return ans

print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))

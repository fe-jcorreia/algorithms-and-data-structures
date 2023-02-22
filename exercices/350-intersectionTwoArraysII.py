def intersect(nums1, nums2):
  seen = {}
  res = []
  for num in nums1:
    seen[num] = 1 + seen.get(num, 0)
  
  for num in nums2:
    if num in seen and seen.get(num, 0) != 0:
      res.append(num)
      seen[num] -= 1
  
  return res
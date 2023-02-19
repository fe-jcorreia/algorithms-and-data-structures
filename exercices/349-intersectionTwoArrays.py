def intersection(nums1, nums2):
  seen = {}
  intersection = {}

  for num in nums1:
    seen[num] = 1 + seen.get(num, 0)

  for num in nums2:
    if seen.get(num, 0) != 0:
      intersection[num] = 1
  
  return intersection.keys()
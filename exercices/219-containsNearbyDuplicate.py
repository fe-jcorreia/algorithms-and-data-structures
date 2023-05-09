def containsNearbyDuplicate(nums, k):
  seen = {}
  
  for j, num in enumerate(nums):
    if num in seen and abs(seen[num] - j) <= k: return True
    seen[num] = j
  
  return False

print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))

def searchRange(nums, target):
  n = len(nums)
  l, r = 0, n - 1

  firstPos = -1
  while l <= r:
    mid = (l + r) // 2
    if target > nums[mid]: l = mid + 1
    if target < nums[mid]: r = mid - 1
    if target == nums[mid]:
      firstPos = mid
      r = mid - 1

  secondPos = -1
  l, r = 0, n - 1
  while l <= r:
    mid = (l + r) // 2
    if target > nums[mid]: l = mid + 1
    if target < nums[mid]: r = mid - 1
    if target == nums[mid]:
      secondPos = mid
      l = mid + 1
  
  return [firstPos, secondPos]

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,8,8,8,9,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([], 0))
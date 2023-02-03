def binarySearch(nums, left, right, target):
  l = left
  r = right
  
  while l <= r:
    mid = (l + r) // 2

    if target > nums[mid]:
      l = mid + 1
    elif target < nums[mid]:
      r = mid - 1
    else:
      return mid
  
  return -1


def search(nums, target):
  left = 0
  right = len(nums) - 1

  while left < right - 1:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
      left = mid
    else:
      right = mid
  
  initialIndex = left if nums[left] < nums[right] else right
  
  if initialIndex == 0:
    return binarySearch(nums, 0, len(nums) - 1, target)
  
  leftSearch = binarySearch(nums, 0, initialIndex - 1, target)
  rightSearch = binarySearch(nums, initialIndex, len(nums) - 1, target)

  return max(leftSearch, rightSearch)

  
print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))
print(search([7,8,0,1,2,3,5,6], 2))

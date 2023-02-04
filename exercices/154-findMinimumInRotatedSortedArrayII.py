def findMinHelper(nums, l, r):
  left = l
  right = r

  while left < right - 1:
    mid = (left + right) // 2

    if nums[right] > nums[mid]:
      right = mid
    elif nums[right] < nums[mid]:
      left = mid
    else:
      return min(findMinHelper(nums, left, mid), findMinHelper(nums, mid, right))
  
  return min(nums[right], nums[left])



def findMin(nums):
  return findMinHelper(nums, 0, len(nums) - 1)


def findMim_opt(nums):
  left = 0
  right = len(nums) - 1

  while left < right - 1:
    mid = (left + right) // 2

    if nums[right] > nums[mid]:
      right = mid
    elif nums[right] < nums[mid]:
      left = mid
    else:
      right -= 1
  
  return min(nums[right], nums[left])


print(findMin([1,3,5]))
print(findMin([2,2,2,0,1]))
print(findMin([4,5,6,0,0,1,2]))
print(findMin([1,8,0,1,1,1,1,1]))
print(findMin([1,1]))
print(findMin([4,5,6,7,0,1,4]))
print(findMin([2,2,2,2,2,2,2,1,2,2,2,2]))
print(findMin([2,2,2,2,0,2,2,2,2,2,2,2]))

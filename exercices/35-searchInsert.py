def searchInsert(nums, target):
  l = 0
  r = len(nums) - 1

  if nums[l] >= target:
    return l

  while (nums[r] != target) and (r - l > 1):
    mid = (r + l) // 2
    if target > nums[mid]:
      l = mid
    else:
      r = mid

  if not nums[r] >= target:
    return r + 1
  
  return r

def searchInsert_opt(nums, target):
  l = 0
  r = len(nums) - 1

  while l <= r:
    mid = (r + l) // 2
    if target > nums[mid]:
      l = mid + 1
    elif target < nums[mid]:
      r = mid - 1
    else:
      return mid
  
  return l

print(searchInsert([1,3,5,6], 5)) # 2
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 7)) # 4
print(searchInsert([1,3,5,6,8,10,15,34,40], 15)) # 6
print(searchInsert([1,3,5,6,8,10,15,34,40], 1)) # 0
print(searchInsert([1,3,5,6,8,10,15,34,40], 40)) # 8
print(searchInsert([1,3,5,6,8,10,15,34,40], 7)) # 4

print("Optmized")
print(searchInsert_opt([1,3,5,6], 5)) # 2
print(searchInsert_opt([1,3,5,6], 2)) # 1
print(searchInsert_opt([1,3,5,6], 7)) # 4
print(searchInsert_opt([1,3,5,6,8,10,15,34,40], 15)) # 6
print(searchInsert_opt([1,3,5,6,8,10,15,34,40], 1)) # 0
print(searchInsert_opt([1,3,5,6,8,10,15,34,40], 40)) # 8
print(searchInsert_opt([1,3,5,6,8,10,15,34,40], 7)) # 4
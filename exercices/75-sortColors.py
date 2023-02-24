def sortColors(nums):
  bucket = [0] * 3

  for num in nums:
    bucket[num] += 1
  
  j = 0
  for i in range(3):
    while bucket[i] != 0:
      nums[j] = i
      bucket[i] -= 1
      j += 1

def swap(array, i, j):
  aux = array[i]
  array[i] = array[j]
  array[j] = aux

def sortColors_opt(nums):
  n = len(nums)
  left = 0
  right = n - 1
  mid = 0

  while mid <= right:
    if nums[mid] == 0:
      swap(nums, mid, left)
      left += 1
      mid += 1
    elif nums[mid] == 1:
      mid += 1
    elif nums[mid] == 2:
      swap(nums, mid, right)
      right -= 1


nums = [2,0,2,1,1,0]
# nums = [2,0,1]
# sortColors(nums)
sortColors_opt(nums)
print(nums)
    


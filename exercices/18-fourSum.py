def fourSum(nums, target):
  nums = sorted(nums)
  res = []
  n = len(nums)

  for a in range(n - 3):
      if a > 0 and nums[a] == nums[a - 1]:
        continue
      for b in range(1, n - 2):
        if b <= a:
          continue
        if b > a + 1 and nums[b] == nums[b - 1]:
          continue

        left = b + 1
        right = n - 1

        while left < right:
          total = nums[a] + nums[b] + nums[left] + nums[right]

          if total < target:
            left += 1
          elif total > target:
            right -= 1
          else:  
            res.append([nums[a], nums[b], nums[left], nums[right]])
            left += 1
            right -= 1
            while nums[left] == nums[left - 1] and left < right:
              left += 1

  return res

# print(fourSum([1,0,-1,0,-2,2], 0))
# print(fourSum([2,2,2,2,2], 8))
print(fourSum([-2,-1,-1,1,1,2,2], 0))

      

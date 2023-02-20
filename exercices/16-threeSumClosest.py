import sys

def threeSumClosest(nums, target):
  nums = sorted(nums)
  n = len(nums)
  closest = sys.maxsize
  
  for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
      total = nums[i] + nums[left] + nums[right]
      
      if total < target:
        left += 1
        while nums[left] == nums[left - 1] and left < right:
          left += 1
      elif total > target:
        right -= 1
        while nums[right] == nums[right + 1] and left < right:
          right -= 1
      else:
        return total

      if abs(total - target) < abs(closest - target):
        closest = total
      
  
  return closest

# [ -4  -1  1  2 ]
print(threeSumClosest([-1,2,1,-4], 1)) # 2
print(threeSumClosest([0,0,0], 1)) # 0
      
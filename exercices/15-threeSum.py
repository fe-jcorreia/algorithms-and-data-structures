def threeSum(nums):
  nums = sorted(nums)
  res = []

  for i in range(len(nums) - 2):
    if i > 0 and nums[i - 1] == nums[i]:
      continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
      total = nums[i] + nums[left] + nums[right]

      if total < 0:
          left += 1
      elif total > 0:
          right -= 1
      else:
        res.append([nums[i], nums[left], nums[right]])
        left += 1

        while nums[left] == nums[left - 1] and left < right:
          left += 1
  
  return res
    

# [-4, -1, -1, 0, 1, 2]
# [-4, -1, -1, 0, 0, 1, 2]
# [-4, -1, -1, 0, 0, 0, 1, 2]
# [-4, -1, -1, 1, 2]


print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,1,1]))


def threeSum_On3(nums):
  res = []
  n = len(nums)

  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      for k in range(n):
        if k == i or k == j:
          continue
          
        if nums[i] + nums[j] + nums[k] == 0:
          isInResponse = False
          for resp in res:
            if nums[i] in resp and nums[j] in resp and nums[k] in resp:
              isInResponse = True

          if not isInResponse:
            res.append([nums[i], nums[j], nums[k]])

  return res

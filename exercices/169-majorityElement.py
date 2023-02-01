def majorityElement(nums):
  seen = {}
  majorityQuantity = (len(nums) // 2) + 1
  
  for num in nums:
    if num not in seen:
      seen[num] = 1
    else:
      seen[num] += 1
      if seen[num] >= majorityQuantity:
        return num
  
  return nums[0]

def majorityElement_opt(nums):
  currentMajority = None
  apparitions = 0
  
  for num in nums:
    if apparitions == 0:
      currentMajority = num
    
    if num == currentMajority:
      apparitions += 1
    else:
      apparitions -= 1
  
  return currentMajority


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2])) 
print(majorityElement([1]))

print(majorityElement_opt([3,2,3]))
print(majorityElement_opt([2,2,1,1,1,2,2])) 
print(majorityElement_opt([1]))
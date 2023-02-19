def containsDuplicate(nums):
  seen = {}

  for num in nums:
    if seen.get(num, 0) != 0:
      return True
    
    seen[num] = 1
  
  return False

def containsDuplicate_opt(nums):
  pass
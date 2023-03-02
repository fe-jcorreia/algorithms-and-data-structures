from sortedcontainers import SortedList

def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
  if not nums or indexDiff <= 0 or valueDiff < 0:
    return False

  mini = min(nums)
  diff = valueDiff + 1  # In case of valueDiff = 0
  bucket = {}

  def getKey(num: int) -> int:
    return (num - mini) // diff

  for i, num in enumerate(nums):
    key = getKey(num)
    if key in bucket:  # Current bucket
      return True
    # Left adjacent bucket
    if key - 1 in bucket and num - bucket[key - 1] < diff:
      return True
    # Right adjacent bucket
    if key + 1 in bucket and bucket[key + 1] - num < diff:
      return True
    bucket[key] = num
    if i >= indexDiff:
      del bucket[getKey(nums[i - indexDiff])]

  return False


print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
# print(containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
# print(containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))




def containsNearbyAlmostDuplicate_sorted_list(nums, indexDiff, valueDiff):
  SList = SortedList()
  for i in range(len(nums)):
    if i > indexDiff:
      SList.remove(nums[i-indexDiff-1])
    
    pos1 = SortedList.bisect_left(SList, nums[i] - valueDiff)
    pos2 = SortedList.bisect_right(SList, nums[i] + valueDiff)
    
    if pos1 != pos2 and pos1 != len(SList):
      return True
    
    SList.add(nums[i])
        
  return False





def containsNearbyAlmostDuplicate_old(nums, indexDiff, valueDiff):
  n = len(nums)
  hasPair = False

  for i, item in enumerate(nums):
    maxCandidate = i + indexDiff
    if maxCandidate >= n:
      maxCandidate = n - 1

    for j in range(i + 1, maxCandidate + 1):
      if abs(item - nums[j]) <= valueDiff:
        hasPair = True
        return hasPair
    
  return hasPair
    
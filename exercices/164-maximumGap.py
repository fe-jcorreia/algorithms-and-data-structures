def maximumGap(nums):
  maxDiff = 0
  n = len(nums)
  maxValue = max(nums)
  minValue = min(nums)

  if n <= 2:
    return maxValue - minValue

  buckets = [[] for _ in range(n)]
  bucketSize = round(((maxValue - minValue) / (n - 1)) + 0.5)
  for item in nums:
    if item != maxValue and item != minValue:
      buckets[(item - minValue) // bucketSize].append(item)
  
  maxBucket = minValue
  for bucket in buckets:
    if not bucket:
      continue
    
    maxDiff = max(maxDiff, min(bucket) - maxBucket)
    maxBucket = max(bucket)
  
  maxDiff = max(maxDiff, maxValue - maxBucket)
  
  return maxDiff
    

# print(maximumGap([3,6,9,1]))
# print(maximumGap([10]))
# print(maximumGap([1,10000000]))
print(maximumGap([1,3,100]))
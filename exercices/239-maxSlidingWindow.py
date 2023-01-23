import sys

def maxSlidingWindow(nums, k):
  maxWindow = []

  for i in range(k - 1, len(nums)):
    currentMax = -sys.maxsize - 1
    for j in range(i + 1 - k, i + 1):
      currentMax = max(currentMax, nums[j])
    
    maxWindow.append(currentMax)
  
  return maxWindow

def maxSlidingWindow_opt(nums, k):
  maxWindow = []
  queue = []
  
  for i, num in enumerate(nums):
      while queue and nums[queue[-1]] <= num:
          queue.pop()
      queue.append(i)
      if i - k == queue[0]: queue.pop(0)
      if i + 1 >= k:
          maxWindow.append(nums[queue[0]])

  return maxWindow
        
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1, -1], 1))

print(maxSlidingWindow_opt([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow_opt([1], 1))
print(maxSlidingWindow_opt([1, -1], 1))
import heapq
import random

def findKthLargest(nums, k): # Time: O(n log n) Space: O(n)
  heap = nums
  heapq.heapify(heap)
  
  while len(heap) != k:
    heapq.heappop(heap)

  return heap[0]

def findKthLargest(nums, k): # Time: O(n log n) Space: O(1)
  n = len(nums)
  nums.sort()
  return nums[n - k]

def findKthLargest_opt(nums, k): # Time: O(n) Space: O(n)
  if not nums: 
    return
  
  pivot = random.choice(nums)
  left =  [x for x in nums if x > pivot]
  mid  =  [x for x in nums if x == pivot]
  right = [x for x in nums if x < pivot]
    
  L, M = len(left), len(mid)
    
  if k <= L:
    return findKthLargest_opt(left, k)
  elif k > L + M:
    return findKthLargest_opt(right, k - L - M)
  else:
    return mid[0]
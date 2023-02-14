import heapq

class KthLargest:
  def __init__(self, k, nums):
    self.k = k
    self.heap = nums
    heapq.heapify(self.heap)

  def add(self, val):
    heapq.heappush(self.heap, val)
    
    while len(self.heap) != self.k:
      heapq.heappop(self.heap)
    
    kthSmallest = self.heap[0]
    
    return kthSmallest

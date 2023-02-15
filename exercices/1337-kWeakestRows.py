import heapq

def binarySearchCount(array):
  l = 0
  r = len(array) - 1
  score = 0

  while l <= r:
    mid = (l + r) // 2

    if array[mid] == 1:
      score += mid - l + 1
      l = mid + 1
    else:
      r = mid - 1
  
  return score

def kWeakestRows(mat, k):
  heap = []

  for i, line in enumerate(mat):
    score = binarySearchCount(line)
    
    heapq.heappush(heap, (score, i))

  return [heapq.heappop(heap)[1] for _ in range(k)]
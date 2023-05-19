import heapq

def kthSmallest(matrix, k):
  heap = []
  n = len(matrix)
  for i in range(0, n):
    heapq.heappush(heap, [matrix[i][0], i, 0])

  count = 0
  while(count < k - 1):
    _, row, col = heapq.heappop(heap)
    
    if( col + 1 < n):
      heapq.heappush(heap, [matrix[row][col + 1], row, col + 1])    
    
    count += 1
  
  return heap[0][0]

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(kthSmallest([[-5]], 1))
print(kthSmallest([[1,2],[1,3]], 1))
print(kthSmallest([[1,2],[1,3]], 2))
print(kthSmallest([[1,2],[1,3]], 3))

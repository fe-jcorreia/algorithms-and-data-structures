import math
import heapq

def pickGifts(gifts, k):
  heap = [-gift for gift in gifts]
  heapq.heapify(heap)

  for _ in range(k):
    num = -heapq.heappop(heap)
    heapq.heappush(heap, -math.floor(math.sqrt(num)))
  
  return -sum(heap)

print(pickGifts([25,64,9,4,100], 4))
print(pickGifts([1,1,1,1], 4))


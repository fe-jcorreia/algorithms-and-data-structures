import heapq

def lastStoneWeight(stones):
  heap = [-i for i in stones]
  heapq.heapify(heap)

  while len(heap) > 1:
    stone1 = heapq.heappop(heap)
    stone2 = heapq.heappop(heap)

    newStone = stone1 - stone2

    heapq.heappush(heap, newStone)

  if not heap:
    return 0
  else:
    return -heap[0]
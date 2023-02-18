import heapq
import sys

def getSkyline(buildings):
  skyline = [[0,0]]
  events = []
  heap = [(0, sys.maxsize)]
  
  for [left, right, height] in buildings:
    heapq.heappush(events, (left, -height, right))
    heapq.heappush(events, (right, 0, 0))
  
  while events:
    x, h, r = heapq.heappop(events)

    while heap[0][1] <= x:
      heapq.heappop(heap)

    if h != 0:
      heapq.heappush(heap, (h, r))

    if skyline[-1][1] != -heap[0][0]:
      skyline.append([x, -heap[0][0]])

  return skyline[1:]

print(getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
print(getSkyline([[0,2,3],[2,5,3]]))
# [[0,3],[5,0]]
import sys
import heapq

def minCostConnectPoints(points):
  points = [tuple(point) for point in points]
  frontierDistance = {point: sys.maxsize for point in points}
  frontierDistance[points[0]] = 0
  heap = [(0, points[0])]
  visited = set()

  totalCost = 0
  while heap:
    cost, currPoint = heapq.heappop(heap)
    if currPoint in visited: continue
    totalCost += cost
    visited.add(currPoint)

    for point in points:
      if point not in visited:
        val = abs(currPoint[0] - point[0]) + abs(currPoint[1] - point[1])
        if frontierDistance[point] > val:
          frontierDistance[point] = val
          heapq.heappush(heap, (val, point))

  return totalCost


print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20
print(minCostConnectPoints([[3,12],[-2,5],[-4,1]])) # 18
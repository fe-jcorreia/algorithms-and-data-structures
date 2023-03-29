import sys
import heapq

def findTheCity(n, edges, distanceThreshold):
  cityNei = [None] * n

  graph = {i: [] for i in range(n)}
  for src, dst, w in edges:
    graph[src].append((dst, w))
    graph[dst].append((src, w))

  for city in range(n):
    totalDistance = [sys.maxsize] * n
    totalDistance[city] = 0

    heap = [(0, city)]

    while heap:
      currDistance, currVertex = heapq.heappop(heap)

      if currDistance > totalDistance[currVertex]:
        continue

      for nextVertex, w in graph[currVertex]:
        if totalDistance[nextVertex] > currDistance + w:
          totalDistance[nextVertex] = currDistance + w
          heapq.heappush(heap, (totalDistance[nextVertex], nextVertex))

    cityNei[city] = [i for i, w in enumerate(totalDistance) if w != 0 and w <= distanceThreshold]
  
  minLen, result = n, 0
  for i, arr in enumerate(cityNei):
    if len(arr) <= minLen:
      minLen = len(arr)
      result = i

  return result

def findTheCity_Floyd_Warshall(n, edges, distanceThreshold):
  dis = [[sys.maxsize] * n for _ in range(n)]
  
  for i, j, w in edges:
    dis[i][j] = dis[j][i] = w
  for i in range(n):
    dis[i][i] = 0

  for k in range(n):
    for i in range(n):
      for j in range(n):
        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

  res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
  return res[min(res)]

print(findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
print(findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
print(findTheCity(6, [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]], 417))
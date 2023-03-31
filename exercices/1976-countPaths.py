import heapq

def countPaths(n, roads):
  graph = {i: [] for i in range(n)}
  for src, dst, w in roads:
    graph[src].append((dst, w))
    graph[dst].append((src, w))

  totalDist = [float('inf')] * n
  heap = [(0, 0)]
  totalDist[0] = 0
  total = [0] * n
  total[0] = 1

  while heap:
    currDist, currVertex = heapq.heappop(heap)
    if currVertex == n - 1: return total[currVertex] % 1000000007

    if currDist > totalDist[currVertex]: continue

    for dst, w in graph[currVertex]:
      if totalDist[dst] == currDist + w:
        total[dst] += total[currVertex]

      if totalDist[dst] > currDist + w:
        totalDist[dst] = currDist + w
        heapq.heappush(heap, (totalDist[dst], dst))
        total[dst] = total[currVertex]


print(countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
print(countPaths(2, [[1,0,10]]))
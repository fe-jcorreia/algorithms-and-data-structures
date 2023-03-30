import heapq

def maxProbability(n, edges, succProb, start, end):
  graph = {i: [] for i in range(n)}
  for i, (src, dst) in enumerate(edges):
    graph[src].append((dst, succProb[i]))
    graph[dst].append((src, succProb[i]))

  totalProb = [0] * n
  totalProb[start] = 1
  heap = [(-1, start)]

  while heap:
    p, currVertex = heapq.heappop(heap)
    currProb = -p

    if currProb < totalProb[currVertex]: continue

    for dst, w in graph[currVertex]:
      if totalProb[dst] < currProb * w:
        totalProb[dst] = currProb * w
        heapq.heappush(heap, (-totalProb[dst], dst))
  
  return round(totalProb[end], 5)

print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
print(maxProbability(3, [[0,1]], [0.5], 0, 2))
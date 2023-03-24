import heapq
import sys

def networkDelayTime(times, n, k):
  graph = {}
  for src, dst, w in times:
    graph.setdefault(src, [])
    graph.setdefault(dst, [])
    graph[src].append((dst, w))

  totalDistance = [sys.maxsize for _ in range(n + 1)]
  totalDistance[k] = 0
  heap = [(0, k)]

  while len(heap):
    currDistance, currVertex = heapq.heappop(heap)

    if currDistance > totalDistance[currVertex]:
      continue

    for dst, w in graph[currVertex]:
      if totalDistance[dst] > currDistance + w:
        totalDistance[dst] = currDistance + w
        heapq.heappush(heap, (totalDistance[dst], dst))

  if sys.maxsize in totalDistance[1:]:
    return -1
    
  return max(totalDistance[1:])

def networkDelayTime_neetcode(times, n, k):
  graph = {}
  for src, dst, w in times:
    graph.setdefault(src, [])
    graph.setdefault(dst, [])
    graph[src].append((dst, w))
  
  heap = [(0, k)]
  visited = set()
  t = 0

  while heap:
    w1, n1 = heapq.heappop(heap)
    if n1 in visited:
      continue
    visited.add(n1)
    t = max(t, w1)
    
    for n2, w2 in graph[n1]:
      if n2 not in visited:
        heapq.heappush(heap, (w1 + w2, n2))

  return t if len(visited) == n else -1

def networkDelayTime_bell(times, n, k):
  totalTime = [sys.maxsize] * (n + 1)
  totalTime[k] = 0

  for _ in range(n - 1):
    for s, d, t in times:
      if totalTime[d] > totalTime[s] + t:
        totalTime[d] = totalTime[s] + t
  
  if sys.maxsize in totalTime[1:]:
    return -1
    
  return max(totalTime[1:])

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(networkDelayTime([[1,2,1]], 2, 1))
print(networkDelayTime([[1,2,1]], 2, 2))
print(networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
import heapq

def longestPathProblem(source):
  topologicalSort = []
  graph = { 
    0: [(1,5), (2,3)],
    1: [(2,2), (3,6)],
    2: [(3,7), (4,4), (5,2)],
    3: [(4,-1), (5,1)],
    4: [(5,-2)],
    5: []
  }

  def dijkstra(graph, source):
    total_distance = [float("inf") for _ in graph]
    total_distance[source] = 0
    heap = [(0, source)]

    while(len(heap) > 0):
      currentDistance, currentVertex = heapq.heappop(heap)

      if currentDistance > total_distance[currentVertex]:
        continue

      for edge in graph[currentVertex]:
        nextVertex, edgeWeight = edge[0], -edge[1]

        if total_distance[nextVertex] > currentDistance + edgeWeight:
          total_distance[nextVertex] = currentDistance + edgeWeight
          heapq.heappush(heap, (total_distance[nextVertex], nextVertex))

    return total_distance
  
  topologicalSort.reverse()
  dist = [-x if x != float('inf') else x for x in dijkstra(graph, source)]

  return dist

print(longestPathProblem(1))
import sys
import heapq

class Dijkstra():
  def execute(self, graph, initialIndex):
    if initialIndex < 0 or initialIndex >= len(graph):
      print("Vértice inválido")
      return

    total_distance = [sys.maxsize for _ in graph]
    total_distance[initialIndex] = 0

    heap = [(0, initialIndex)]

    parent = [None for _ in graph]

    while(len(heap) > 0):
      currentDistance, currentVertex = heapq.heappop(heap)

      if currentDistance > total_distance[currentVertex]:
        continue

      for edge in graph[currentVertex]:
        nextVertex = edge[1]
        edgeWeight = edge[2]

        if total_distance[nextVertex] > currentDistance + edgeWeight:
          total_distance[nextVertex] = currentDistance + edgeWeight
          parent[nextVertex] = currentVertex
          heapq.heappush(heap, (total_distance[nextVertex], nextVertex))

    print("================ RESULT ================")
    print("FROM INDEX", initialIndex)
    print("\ndistance: ", total_distance)
    print("\nparent: ", parent)

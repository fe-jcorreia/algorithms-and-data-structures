import sys
import heapq

class Prim():
  def execute(self, graph, initialIndex):
    if initialIndex < 0 or initialIndex >= len(graph):
      print("Vértice inválido")
      return

    frontier_distance = [sys.maxsize for _ in graph]
    frontier_distance[initialIndex] = 0

    heap = [(0, initialIndex)]

    parent = [None for _ in graph]

    status = [False for _ in graph]

    while(len(heap) > 0):
      _, currentVertex = heapq.heappop(heap)
      status[currentVertex] = True

      for edge in graph[currentVertex]:
        nextVertex = edge[1]
        edgeWeight = edge[2]

        if frontier_distance[nextVertex] > edgeWeight and status[nextVertex] == False:
          frontier_distance[nextVertex] = edgeWeight
          heapq.heappush(heap, (frontier_distance[nextVertex], nextVertex))
          parent[nextVertex] = currentVertex

    print("================ RESULT ================")
    print("FROM INDEX", initialIndex)
    print("\nparent: ", parent)

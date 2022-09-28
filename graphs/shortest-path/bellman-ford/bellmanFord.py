import sys

class BellmanFord():
  def execute(self, graph, initialIndex):
    if initialIndex < 0 or initialIndex >= len(graph):
      print("Vértice inválido")
      return

    total_distance = [sys.maxsize for _ in graph]
    total_distance[initialIndex] = 0

    parent = [None for _ in graph]

    for _ in range(len(graph) - 1):
      for vertex in graph:
        for edge in vertex:
          currentVertex = edge[0]
          currentDistance = total_distance[currentVertex]
          nextVertex = edge[1]
          edgeWeight = edge[2]

          if total_distance[nextVertex] > currentDistance + edgeWeight:
            total_distance[nextVertex] = currentDistance + edgeWeight
            parent[nextVertex] = currentVertex
    
    for vertex in graph:
        for edge in vertex:
          currentVertex = edge[0]
          currentDistance = total_distance[currentVertex]
          nextVertex = edge[1]
          edgeWeight = edge[2]

          if total_distance[nextVertex] > currentDistance + edgeWeight:
            print("================ RESULT ================")
            print("Cicle encountered, ending processing...")
            print("\nFROM INDEX", initialIndex)
            print("\ndistance: ", total_distance)
            print("\nparent: ", parent)
            return

    print("================ RESULT ================")
    print("FROM INDEX", initialIndex)
    print("\ndistance: ", total_distance)
    print("\nparent: ", parent)

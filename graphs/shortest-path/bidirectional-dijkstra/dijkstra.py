import sys
import heapq

class Dijkstra():
  def print_shortest_path(self, initialIndex, searchVertex, best_vertex, forward_parent, reverse_parent):
    print("================ RESULT ================")
    print(f"Path: {initialIndex} -> {searchVertex}")

    path = []
    last = best_vertex
    while forward_parent[last] != None:
      path.append(last)
      last = forward_parent[last]
    path.append(initialIndex)
    path.reverse()
    last = best_vertex
    while reverse_parent[last] != None:
      last = reverse_parent[last]
      path.append(last)
    
    print(path)

  def process_shortest_path(self, initialIndex, searchVertex, forward_parent, reverse_parent, forward_distance, reverse_distance, forward_processed, reverse_processed):
    distance = sys.maxsize
    best_vertex = None
    
    for vertex in forward_processed + reverse_processed:
      if forward_distance[vertex] + reverse_distance[vertex] < distance:
        best_vertex = vertex
        distance = forward_distance[vertex] + reverse_distance[vertex]
    
    self.print_shortest_path(initialIndex, searchVertex, best_vertex, forward_parent, reverse_parent)

  def execute(self, graph, initialIndex, searchVertex):
    if initialIndex < 0 or initialIndex >= len(graph):
      print("Vértice inválido")
      return
    if searchVertex < 0 or searchVertex >= len(graph):
      print("Vértice inválido")
      return

    forward_distance = []
    reverse_distance = []
    forward_parent = []
    reverse_parent = []

    for _ in graph:
      forward_distance.append(sys.maxsize)
      reverse_distance.append(sys.maxsize)
      forward_parent.append(None)
      reverse_parent.append(None)

    forward_distance[initialIndex] = 0
    reverse_distance[searchVertex] = 0
    forward_heap = [(0, initialIndex)]
    reverse_heap = [(0, searchVertex)]

    forward_processed = []
    reverse_processed = []

    while True:
      currentDistance, currentVertex = heapq.heappop(forward_heap)

      for edge in graph[currentVertex]:
        nextVertex = edge[1]
        edgeWeight = edge[2]

        if forward_distance[nextVertex] > currentDistance + edgeWeight:
          forward_distance[nextVertex] = currentDistance + edgeWeight
          forward_parent[nextVertex] = currentVertex
          heapq.heappush(forward_heap, (forward_distance[nextVertex], nextVertex))
      
      forward_processed.append(currentVertex)
      
      if currentVertex in reverse_processed: 
        self.process_shortest_path(initialIndex, searchVertex, forward_parent, reverse_parent, forward_distance, reverse_distance, forward_processed, reverse_processed)
        break

      currentDistance, currentVertex = heapq.heappop(reverse_heap)

      for edge in graph[currentVertex]:
        nextVertex = edge[1]
        edgeWeight = edge[2]

        if reverse_distance[nextVertex] > currentDistance + edgeWeight:
          reverse_distance[nextVertex] = currentDistance + edgeWeight
          reverse_parent[nextVertex] = currentVertex
          heapq.heappush(reverse_heap, (reverse_distance[nextVertex], nextVertex))
      
      reverse_processed.append(currentVertex)
      
      if currentVertex in forward_processed: 
        self.process_shortest_path(initialIndex, searchVertex, forward_parent, reverse_parent, forward_distance, reverse_distance, forward_processed, reverse_processed)
        break

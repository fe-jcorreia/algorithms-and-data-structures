def longestPathProblem(source):
  visited = set()
  topologicalSort = []
  graph = { 
    0: [(1,5), (2,3)],
    1: [(2,2), (3,6)],
    2: [(3,7), (4,4), (5,2)],
    3: [(4,-1), (5,1)],
    4: [(5,-2)],
    5: []
  }

  def sort(graph, initialVertex):
    visited.add(initialVertex)

    for edge in graph[initialVertex]:
      if not (edge[0] in visited):
        sort(graph, edge[0])

    topologicalSort.append(initialVertex)

  def dijkstra(graph, source):
    dist = [float("inf") for _ in range(len(graph))]

    dist[source] = 0
    for vertex in topologicalSort:
      pass

  sort(graph, 0)
  topologicalSort.reverse()



longestPathProblem(1)
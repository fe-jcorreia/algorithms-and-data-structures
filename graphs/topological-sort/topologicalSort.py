from checkCicle import CheckCicle

class TopologicalSort():
  def sort(self, graph, initialVertex, status, topologicalSort):
    status[initialVertex] = 'D'

    for edge in graph[initialVertex]:
      nextVertex = edge[1]
      
      if status[nextVertex] == 'U':
        self.sort(graph, nextVertex, status, topologicalSort)
   
    status[initialVertex] = 'P'
    topologicalSort.append(initialVertex)

  def topological_sort(self, graph, initialVertex):
    status = ['U' for _ in graph]
    topologicalSort = []

    self.sort(graph, initialVertex, status, topologicalSort)
    topologicalSort.reverse()

    return topologicalSort

  def execute(self, graph): 
    checkCicle = CheckCicle()
    if checkCicle.execute(graph):
      return None

    return self.topological_sort(graph, 0)

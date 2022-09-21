class CheckCicle():
  def checkCicle(self, graph, initialVertex, status, parent, hasCicle):
    status[initialVertex] = 'D'

    for edge in graph[initialVertex]:
      nextVertex = edge[1]
      
      if status[nextVertex] == 'U':
        parent[nextVertex] = initialVertex
        hasCicle = self.checkCicle(graph, nextVertex, status, parent, hasCicle)
      elif status[nextVertex] == 'D' and parent[initialVertex] != nextVertex:
        return True
   
    status[initialVertex] = 'P'
    return hasCicle

  def execute(self, graph): 
    status = ['U' for _ in graph]
    parent = [None for _ in graph]
    
    initialVertex = 0
    hasCicle = False
    hasCicle = self.checkCicle(graph, initialVertex, status, parent, hasCicle)

    return hasCicle

import queue

class CheckBipartite():
  def getComplement(self, vertexColor):
      if vertexColor == 'white': return 'black'
      if vertexColor == 'black': return 'white'

      return None

  def checkBipartite(self, graph, initialVertex, status, color):  
    q = queue.Queue()

    status[initialVertex] = 'D'
    color[initialVertex] = 'white'
    q.put(initialVertex)

    while(not q.empty()):
      currentVertex = q.get()

      for edge in graph[currentVertex]:
        nextVertex = edge[1]

        if status[nextVertex] == 'U':
          status[nextVertex] = 'D'
          color[nextVertex] = self.getComplement(color[currentVertex])
          q.put(nextVertex)
          
        if status[nextVertex] != 'P':
          if color[nextVertex] == color[currentVertex]:
            return False

      status[currentVertex] = 'P'
    
    return True

  def execute(self, graph): 
    color = [None for _ in graph]
    status = ['U' for _ in graph]
    isBipartite = True
    
    for index, _ in enumerate(graph):
      if status[index] == 'U':
        isBipartite = self.checkBipartite(graph, index, status, color)

        if not isBipartite:
          break

    return isBipartite

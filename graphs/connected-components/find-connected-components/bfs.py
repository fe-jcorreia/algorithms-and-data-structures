import queue

class BreadthFirstSearch():
  def execute(self, graph, initialVertex, status):
    if initialVertex < 0 or initialVertex >= len(graph):
      print("Vértice inválido")
      return
    
    q = queue.Queue()
    parent = [None for _ in graph]

    status[initialVertex] = 'D'
    q.put(initialVertex)

    while(not q.empty()):
      currentVertex = q.get()

      for edge in graph[currentVertex]:
        nextVertex = edge[1]
        
        if status[nextVertex] == 'U':
          status[nextVertex] = 'D'
          q.put(nextVertex)
          parent[nextVertex] = currentVertex
      
      status[currentVertex] = 'P'
    
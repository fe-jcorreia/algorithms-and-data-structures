import queue

class BreadthFirstSearch():
  def processVertexInit(self, v: int):
    print(f"Starting vertex {v} processing...")
  
  def processVertexEnd(self, v: int):
    print(f"Vertex {v} processed.")
  
  def processEdge(self, v: int, w: int):
    print(f"Edge ({v}, {w}) processed.")

  def execute(self, graph, initialVertex):
    if initialVertex < 0 or initialVertex >= len(graph):
      print("Vértice inválido")
      return
    
    q = queue.Queue()
    status = ['U' for _ in graph]
    parent = [None for _ in graph]

    status[initialVertex] = 'D'
    q.put(initialVertex)

    while(not q.empty()):
      currentVertex = q.get()

      self.processVertexInit(currentVertex)

      for edge in graph[currentVertex]:
        nextVertex = edge[1]

        if status[nextVertex] != 'P':
          self.processEdge(currentVertex, nextVertex)
        
        if status[nextVertex] == 'U':
          status[nextVertex] = 'D'
          q.put(nextVertex)
          parent[nextVertex] = currentVertex
      
      self.processVertexEnd(currentVertex)
      status[currentVertex] = 'P'
    
    print("BFS Endend.")

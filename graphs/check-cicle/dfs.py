class DepthFirstSearch():
  def processVertexInit(self, v: int):
    print(f"Starting vertex {v} processing...")
  
  def processVertexEnd(self, v: int):
    print(f"Vertex {v} processed.")
  
  def processEdge(self, v: int, w: int):
    print(f"Edge ({v}, {w}) processed.")

  def dfs(self, graph, initialVertex, status, parent):
    status[initialVertex] = 'D'
    self.processVertexInit(initialVertex)

    for edge in graph[initialVertex]:
      nextVertex = edge[1]
      
      if status[nextVertex] == 'U':
        parent[nextVertex] = initialVertex
        self.processEdge(initialVertex, nextVertex)
        self.dfs(graph, nextVertex, status, parent)
      elif status[nextVertex] == 'D' and parent[initialVertex] != nextVertex:
        self.processEdge(initialVertex, nextVertex)
   
    status[initialVertex] = 'P'
    self.processVertexEnd(initialVertex)

  def execute(self, graph, initialVertex):
    if initialVertex < 0 or initialVertex >= len(graph):
      print("Vértice inválido")
      return
    
    status = ['U' for _ in graph]
    parent = [None for _ in graph]


    self.dfs(graph, initialVertex, status, parent)
    
    print("DFS Endend.")

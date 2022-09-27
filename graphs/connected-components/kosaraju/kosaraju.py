class Kosaraju():
  def dfs(self, graph, initialVertex, status, stack):
    status[initialVertex] = 'D'

    for edge in graph[initialVertex]:
      nextVertex = edge[1]
      
      if status[nextVertex] == 'U':
        self.dfs(graph, nextVertex, status, stack)
   
    status[initialVertex] = 'P'
    stack.append(initialVertex)
  
  def listStronglyConnected(self, graph, initialVertex, status, stronglyConnected):
    status[initialVertex] = 'D'

    for edge in graph[initialVertex]:
      nextVertex = edge[1]
      
      if status[nextVertex] == 'U':
        stronglyConnected.append(self.listStronglyConnected(graph, nextVertex, status, stronglyConnected))
   
    status[initialVertex] = 'P'
    return initialVertex


  def execute(self, graph): 
    status = ['U' for _ in graph]
    stack = []

    for index, _ in enumerate(graph):
      if(status[index] == 'U'):
        self.dfs(graph, index, status, stack)

    newGraph = [[] for _ in graph]
    for vertex in graph:
      for edge in vertex:
        newTuple = (edge[1], edge[0], edge[2])
        newGraph[newTuple[0]].append(newTuple)
    
    status = ['U' for _ in graph]
    allComponents = []
    while len(stack) > 0:
      initialVertex = stack.pop() 
      if(status[initialVertex] == 'U'):
        stronglyConnected = []
        stronglyConnected.append(self.listStronglyConnected(newGraph, initialVertex, status, stronglyConnected))
        allComponents.append(stronglyConnected)
    
    return allComponents
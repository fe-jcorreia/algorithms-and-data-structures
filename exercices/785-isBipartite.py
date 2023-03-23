def checkBipartite(graph, status, initialVertex, color):
  q = []
  status[initialVertex] = 'D'
  color[initialVertex] = 'R'
  q.append(initialVertex)

  def getComplement(color):
    if color == 'R': return 'B'
    elif color == 'B': return 'R'
  
  while q:
    currVertex = q.pop(0)

    for nextVertex in graph[currVertex]:
      if status[nextVertex] == 'U':
        color[nextVertex] = getComplement(color[currVertex]) 
        status[nextVertex] = 'D'
        q.append(nextVertex)
      
      if status[nextVertex] == 'D':
        if color[currVertex] == color[nextVertex]: return False
      
    status[currVertex] = 'P'

  return True


def isBipartite(graph):
  status = ['U'] * len(graph)
  color = [None] * len(graph)

  for i in range(len(graph)):
    if status[i] == 'U':
      result = checkBipartite(graph, status, i, color)
      if not result: return False

  return True

print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))
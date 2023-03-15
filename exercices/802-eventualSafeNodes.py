def dfs(graph, status, initialVertex, safeNodes):
  status[initialVertex] = 'D'

  for nextVertex in graph[initialVertex]:
    if status[nextVertex] == 'U':
      safeVertex = dfs(graph, status, nextVertex, safeNodes)
      if not safeVertex: return False
    if status[nextVertex] == 'D':
      return False

  status[initialVertex] = 'P'
  safeNodes.append(initialVertex)
  return True

def eventualSafeNodes_old(graph):
  status = ['U' for _ in graph]
  safeNodes = []

  for i in range(len(graph)):
    if status[i] == 'U':
      dfs(graph, status, i, safeNodes)
    
  return sorted(safeNodes)

def eventualSafeNodes(graph):
  n = len(graph)
  safe = {}

  def dfs(i):
    if i in safe:
      return safe[i]
    safe[i] = False
    for nextVertex in graph[i]:
      if not dfs(nextVertex):
        return safe[i]
    safe[i] = True
    return safe[i]
  
  res = []
  for i in range(n):
    if dfs(i):
      res.append(i)
  
  return res

print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
def isPrintable(targetGrid):
  m = len(targetGrid)
  n = len(targetGrid[0])
  graph = {}

  for color in range(1, 61):
    l, r, t, b = n, -1, m, -1
    for i in range(m):
      for j in range(n):
        if targetGrid[i][j] == color:
          l = min(l, j)
          r = max(r, j)
          t = min(t, i)
          b = max(b, i)
    
    for i in range(t, b + 1):
      for j in range(l, r + 1):
        if targetGrid[i][j] != color:
          graph.setdefault(targetGrid[i][j], set()).add(color)
  

  status = ['U'] * 61
  def isValid(v):
    if v not in graph: return True
    status[v] = 'D'

    for dst in graph[v]:
      if status[dst] == 'U':
        valid = isValid(dst)
        if not valid: return False
      if status[dst] == 'D':
        return False
    
    status[v] = 'P'
    return True

  for v in graph:
    if status[v] == 'U':
      valid = isValid(v)
      if not valid: return False
  
  return True

print(isPrintable([[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]))
print(isPrintable([[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]))
print(isPrintable([[1,2,1],[2,1,2],[1,2,1]]))
print(isPrintable([[1,1,1],[3,1,3]]))
print(isPrintable([[6,2,2,5],[2,2,2,5],[2,2,2,5],[4,3,3,4]]))

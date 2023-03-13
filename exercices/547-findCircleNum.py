def bfs(graph, visited, initialVertex):
  q = []
  n = len(graph[0])
  visited.add(initialVertex)
  q.append(initialVertex)

  while q:
    curVertex = q.pop()
    for nextVertex in range(n):
      if graph[curVertex][nextVertex] == 1 and nextVertex not in visited:
        visited.add(nextVertex)
        q.append(nextVertex)

def findCircleNum(isConnected):
  n = len(isConnected[0])
  visited = set()
  connectedComponents = 0

  for i in range(n):
    if i not in visited:
      bfs(isConnected, visited, i)
      connectedComponents += 1
    
  return connectedComponents

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
print(findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
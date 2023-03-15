def hasCicle(graph, visiting, initialVertex, parent):
  visiting.add(initialVertex)

  for nextVertex in graph[initialVertex]:
    if nextVertex not in visiting:
      parent[nextVertex] = initialVertex
      cicle = hasCicle(graph, visiting, nextVertex, parent)
      if cicle: return True
    elif parent.get(initialVertex) != nextVertex:
      return True

  return False
    

def findRedundantConnection_old(edges):
  adjList = {}
  for edge in edges:
    adjList.setdefault(edge[0], []).append(edge[1])
    adjList.setdefault(edge[1], []).append(edge[0])

  for edge in reversed(edges):
    adjList[edge[1]].remove(edge[0])
    adjList[edge[0]].remove(edge[1])

    parent = {}
    visiting = set()
    if not hasCicle(adjList, visiting, 1, parent) and len(visiting) == len(adjList):
      return edge
    
    adjList[edge[1]].append(edge[0])
    adjList[edge[0]].append(edge[1])

def findRedundantConnection(edges):
  n = len(edges)
  parent = [i for i in range(n + 1)]
  rank = [1] * n + 1

  def find(n):
    p = parent[n]
    while p != parent[p]:
      parent[p] = parent[parent[p]]
      p = parent[p]
    return p
  
  def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
      return False
    if rank[p1] > rank[p2]:
      parent[p2] = p1
      rank[p1] += rank[p2]
    else:
      parent[p1] = p2
      rank[p2] += rank[p1]
    return True
  
  for n1, n2 in edges:
    if not union(n1, n2):
      return [n1, n2]
    

  
print(findRedundantConnection([[1,2],[1,3],[2,3]]))
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]]))
    
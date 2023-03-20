def findRedundantDirectedConnection(edges):
  n = len(edges)
  parent = [i for i in range(n + 1)]
  rank = [1] * (n + 1)

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
  
  cand1, cand2, point_to = None, None, {}
  for node1, node2 in edges:
    if node2 in point_to: 
      cand1, cand2 = point_to[node2], [node1, node2]
      break
    point_to[node2] = [node1, node2]
      
  for node1, node2 in edges:
    if [node1, node2] == cand2: continue
    if not union(node1, node2):
      if cand1: return cand1
      return [node1, node2]
  return cand2



print(findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))
print(findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
print(findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
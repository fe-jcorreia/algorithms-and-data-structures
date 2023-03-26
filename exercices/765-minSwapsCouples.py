def minSwapsCouples(row):
  n = len(row) // 2
  graph = {}
  coupleOf = {}

  graphPermutationVertex = 0
  for i in range(n):
    coupleOf[2*i] = graphPermutationVertex
    coupleOf[2*i + 1] = graphPermutationVertex
    graph[graphPermutationVertex] = set()
    graphPermutationVertex += 1

  for p in range(n):
    graph[coupleOf[row[2*p]]].add(coupleOf[row[2*p + 1]])
    graph[coupleOf[row[2*p + 1]]].add(coupleOf[row[2*p]])

  parent = [i for i in range(len(graph))]
  rank = [1] * len(graph)
  def find(v):
    p = parent[v]
    while p != parent[p]:
      parent[p] = parent[parent[p]]
      p = parent[p]
    return p      
  
  def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
      return 0
    if rank[p1] > rank[p2]:
      parent[p2] = p1
      rank[p1] += rank[p2]
    else:
      parent[p1] = p2
      rank[p2] += rank[p1]
    return 1

  conComp = len(graph)
  for src in graph:
    for dst in graph[src]:
      conComp -= union(src, dst)

  return len(graph) - conComp

print(minSwapsCouples([0,2,1,3]))
print(minSwapsCouples([3,2,0,1]))
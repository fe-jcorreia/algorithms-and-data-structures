def dfs(graph, visiting, initialVertex, target):
  if not graph.get(initialVertex) or not graph.get(target):
    return -1.0
  
  if initialVertex == target:
    return 1.0

  visiting.add(initialVertex)
  curW = -1.0
  for nextVertex, w in graph[initialVertex]:
    if nextVertex not in visiting:
      curW = max(curW, w * dfs(graph, visiting, nextVertex, target))
  
  if curW < 0:
      return -1.0
  return curW
    
def calcEquation(equations, values, queries):
    graph = {}
    result = []

    for i, edge in enumerate(equations):
      graph.setdefault(edge[0], []).append((edge[1], values[i]))
      graph.setdefault(edge[1], []).append((edge[0], 1.0 / values[i]))

    for item in queries:
      visiting = set()
      result.append(dfs(graph, visiting, item[0], item[1]))
        
    return result
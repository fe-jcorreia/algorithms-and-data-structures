def allPathsSourceTarget(graph):
  n = len(graph)
  result = []
  currPath = []

  def dfs(initialVertex):
    currPath.append(initialVertex)

    for nextVertex in graph[initialVertex]:
      dfs(nextVertex)
      currPath.pop()

    if initialVertex == n - 1:
      result.append(currPath.copy())

  dfs(0)

  return result

print(allPathsSourceTarget([[1,2],[3],[3],[]]))
print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
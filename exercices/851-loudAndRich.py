def topologicalSort(graph, initialVertex, quiet, richSort):
  curPerson = initialVertex
  for nextVertex in graph[initialVertex]:
    if richSort[nextVertex] == None:
      topologicalSort(graph, nextVertex, quiet, richSort)
    curPerson = min(curPerson, richSort[nextVertex], key=lambda x: quiet[x])

  richSort[initialVertex] = curPerson

def loudAndRich(richer, quiet):
  n = len(quiet)
  ans = [None for _ in range(n)]

  adjList = {i: set() for i in range(n)}
  for p1, p2 in richer:
    adjList[p2].add(p1)
  
  for i in range(n):
    if ans[i] == None:
      topologicalSort(adjList, i, quiet, ans)

  return ans

print(loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]))
print(loudAndRich([], [0]))
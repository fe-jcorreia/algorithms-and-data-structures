def findMinHeightTrees(n, edges):
  if n <= 0:
    return []

  if n == 1:
    return [0]
  
  adjList = {i: set() for i in range(n)}
  for edge in edges:
    adjList[edge[0]].add(edge[1])
    adjList[edge[1]].add(edge[0])
 
  leaves = [i for i in range(n) if len(adjList[i]) == 1]
  curValidNodes = n

  while curValidNodes > 2:
    newLeaves = []

    for leaf in leaves:
      neighbor = adjList[leaf].pop()
      adjList[neighbor].remove(leaf)

      if len(adjList[neighbor]) == 1:
        newLeaves.append(neighbor)
      
    curValidNodes -= len(leaves)
    leaves = newLeaves

  return leaves

print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))

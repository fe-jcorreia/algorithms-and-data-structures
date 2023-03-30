import heapq

def countRestrictedPaths(n, edges):
  graph = {i: [] for i in range(n + 1)}
  for src, dst, w in edges:
    graph[src].append((dst, w))
    graph[dst].append((src, w))
  
  totalDist = [None] * (n + 1)
  totalDist[n] = 0
  heap = [(0, n)]
  visited = set()

  while heap:
    currDist, currVertex = heapq.heappop(heap)
    if currVertex in visited: continue
    visited.add(currVertex)
    
    for dst, w in graph[currVertex]:
      if dst not in visited:
        if totalDist[dst] == None or totalDist[dst] > currDist + w:
          totalDist[dst] = currDist + w
          heapq.heappush(heap, (totalDist[dst], dst))

  def dfs(v, memo):
    if memo[v] != None: return memo[v]
    if v == n: return 1

    ans = 0
    for dst, _ in graph[v]:
      if totalDist[dst] < totalDist[v]:
        ans = (ans + dfs(dst, memo)) % 1000000007
    
    memo[v] = ans
    return ans

  return dfs(1, [None] * (n + 1))

print(countRestrictedPaths(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))
print(countRestrictedPaths(7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))
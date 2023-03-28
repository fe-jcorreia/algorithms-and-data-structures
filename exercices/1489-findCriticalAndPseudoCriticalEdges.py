import collections
import sys

def find(parent, v):
    p = parent[v]
    while p != parent[p]:
      parent[p] = parent[parent[p]]
      p = parent[p]
    return p
  
def union(parent, rank, v1, v2):
  p1, p2 = find(parent, v1), find(parent, v2)
  if p1 == p2:
    return False
  if rank[p1] > rank[p2]:
    parent[p2] = p1
    rank[p1] += rank[p2]
  else:
    parent[p1] = p2
    rank[p2] += rank[p1]
  return True

def findCriticalAndPseudoCriticalEdges(n, edges):
  edges = [(src, dst, w, i) for i, (src, dst, w) in enumerate(edges)]
  edges.sort(key=lambda x: x[2])
  
  def totalWeightWithoutEdge(index):
    parent = [i for i in range(n)]
    rank = [1] * n

    ans = 0
    for i, (src, dst, w, _) in enumerate(edges):
      if i == index:
        continue
      if union(parent, rank, src, dst):
        ans += w

    p = find(parent, 0)
    return ans if all(find(parent, i) == p for i in range(n)) else sys.maxsize
  
  def totalWeightWithEdge(index):
    parent = [i for i in range(n)]
    rank = [1] * n

    src0, dst0, w0, _ = edges[index]
    ans = w0
    union(parent, rank, src0, dst0)
    for i, (src, dst, w, _) in enumerate(edges):
      if i == index:
        continue
      if union(parent, rank, src, dst):
        ans += w
    
    p = find(parent, 0)
    return ans if all(find(parent, i) == p for i in range(n)) else sys.maxsize
  
  baseWeight = totalWeightWithoutEdge(-1)
  crit, psCrit = set(), set()
  for i in range(len(edges)):
    if totalWeightWithoutEdge(i) > baseWeight: crit.add(edges[i][3])
    elif totalWeightWithEdge(i) == baseWeight: psCrit.add(edges[i][3])

  return [list(crit), list(psCrit)]

def findCriticalAndPseudoCriticalEdges_old(n, edges):
  def dfs(curr, level, parent):
    levels[curr] = level
    for child, i in graph[curr]:
      if child == parent:
        continue
      elif levels[child] == -1:
        levels[curr] = min(levels[curr], dfs(child, level + 1, curr))
      else:
        levels[curr] = min(levels[curr], levels[child])
      if levels[child] >= level + 1 and i not in p_cri:
        cri.add(i)
    return levels[curr]

  # init critical and pseudo-critical edge set
  cri, p_cri = set(), set()

  # use dic to store all edges associated with a given weight
  dic = {}
  for i, (u, v, w) in enumerate(edges):
      dic.setdefault(w, []).append([u, v, i])

  # define union find et
  parent = [i for i in range(n)]
  rank = [1] * n

  # iterate through all weights in ascending order
  for w in sorted(dic):   
    # seen[(pu, pv)] contains all edges connecting pu and pv,
    # where pu and pv are the parent nodes of their corresponding groups
    seen = collections.defaultdict(set)
    # populate seen
    for u, v, i in dic[w]:
      pu, pv = find(parent, u), find(parent, v)
      # skip the edge that creates cycle
      if pu == pv:
        continue
      seen[min(pu, pv), max(pu, pv)].add(i) # edge i connects pu and pv
    
    # w_edges contains all weight-w edges we may add to MST
    w_edges, graph = [], collections.defaultdict(list)
    for pu, pv in seen:
      # more than 1 edge can connect pu and pv
      # these edges are pseudo-critical
      if len(seen[pu, pv]) > 1:
        p_cri |= seen[pu, pv]
      # construct graph for weight w 
      edge_idx = seen[pu, pv].pop()
      graph[pu].append((pv, edge_idx))
      graph[pv].append((pu, edge_idx))
      w_edges.append((pu, pv, edge_idx))
      # union pu and pv groups
      union(parent, rank, pu, pv)
    
    # run dfs to mark all critical w_edges
    levels = [-1] * n
    for u, v, i in w_edges:
      if levels[u] == -1:
        dfs(u, 0, -1)
    # the edges in w_edges cycles are pseudo-critical
    for u, v, i in w_edges:
      if i not in cri:
        p_cri.add(i)

  return [list(cri), list(p_cri)]


print(findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
print(findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))
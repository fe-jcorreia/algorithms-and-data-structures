class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

def clone(node, visited):
  if not node:
    return
  
  newGraph = Node(node.val)
  visited[node] = newGraph

  for n in node.neighbors:
    if n in visited:
      newGraph.neighbors.append(visited[n])
    else:
      newGraph.neighbors.append(clone(n, visited))
  
  return newGraph

def cloneGraph(node):
  visited = {}
  return clone(node, visited)

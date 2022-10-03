import heapq

class Kruskal():
  def searchRoot(self, parent, i):
    if parent[i] == None:
      return i
    return self.searchRoot(parent, parent[i])

  def execute(self, graph):
    heap = [(edge[2], edge[0], edge[1]) for vertex in graph for edge in vertex]
    heapq.heapify(heap)

    union_find = []
    height = []
    result = []

    for _ in graph: 
      union_find.append(None)
      height.append(1)

    while(len(heap) > 0):
      edgeWeight, currentVertex, nextVertex = heapq.heappop(heap)

      rootCurrentVertex = self.searchRoot(union_find, currentVertex)
      rootNextVertex = self.searchRoot(union_find, nextVertex)

      if rootCurrentVertex != rootNextVertex:
        if height[rootCurrentVertex] < height[rootNextVertex]:
          union_find[rootCurrentVertex] = rootNextVertex
        elif height[rootCurrentVertex] > height[rootNextVertex]:
          union_find[rootNextVertex] = rootCurrentVertex
        else:
          union_find[rootNextVertex] = rootCurrentVertex
          height[rootCurrentVertex] += 1

        result.append((currentVertex, nextVertex, edgeWeight))

    print("================ RESULT ================")
    print("edges: ", result)

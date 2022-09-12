import sys
from heap import Heap

def get_min_distance(distance_list, status):
  min_item = sys.maxsize
  min_index = -1
  for index, item in enumerate(distance_list):
    if min_item >= item and status[index] == False:
      min_item = item
      min_index = index

  return min_item, min_index

def dijkstra(graph, initialIndex):
  if initialIndex < 0 or initialIndex >= len(graph):
    print("Vértice inválido")
    return
  
  heap = Heap()
  for index, _ in enumerate(graph):
    if index == initialIndex:
      heap.insert_on_heap(0, index)
    else:
      heap.insert_on_heap(sys.maxsize, index)

  total_distance = [sys.maxsize for _ in graph]
  total_distance[initialIndex] = 0

  parent = [-1 for _ in graph]

  status = [False for _ in graph]

  while(not heap.is_empty_heap()):
    _, currentVertex = get_min_distance(total_distance, status)

    for edge in graph[currentVertex]:
      nextVertex = edge[1]
      edgeWeight = edge[2]

      if status[nextVertex] != True:

        if total_distance[nextVertex] > total_distance[currentVertex] + edgeWeight:
          total_distance[nextVertex] = total_distance[currentVertex] + edgeWeight
          parent[nextVertex] = currentVertex

    status[currentVertex] = True

  print("================ RESULT ================")
  print("FROM INDEX", initialIndex)
  print("\ndistance: ", total_distance)
  print("\nparent: ", parent)

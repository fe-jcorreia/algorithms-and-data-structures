import sys

def get_min_distance(distance_list):
  min_item = sys.maxsize
  min_index = -1
  for item in distance_list:
    if min_item >= item[0]:
      min_item = item[0]
      min_index = item[1]

  return min_item, min_index

def get_vertex_index(distance_list, index):
  for d_index, item in enumerate(distance_list):
    if (item[1] == index):
      return d_index

def dijkstra(graph, initialIndex):
  if initialIndex < 0 or initialIndex >= len(graph):
    print("Vértice inválido")
    return

  distance = [[sys.maxsize, index] for index, _ in enumerate(graph)]
  distance[initialIndex] = [0, initialIndex]

  total_distance = [sys.maxsize for _ in graph]
  total_distance[initialIndex] = 0

  parent = [0 for _ in graph]
  parent[initialIndex] = -1

  status = [False for _ in graph]

  while(len(distance) != 0):
    _, currentVertex = get_min_distance(distance)

    for edge in graph[currentVertex]:
      nextVertex = edge[1]

      if status[nextVertex] != True:
        currentDistanceIndex = get_vertex_index(distance, currentVertex)
        nextDistanceIndex = get_vertex_index(distance, edge[1])
        edgeWeight = edge[2]

        if distance[nextDistanceIndex][0] > distance[currentDistanceIndex][0] + edgeWeight:
          distance[nextDistanceIndex][0] = distance[currentDistanceIndex][0] + edgeWeight
          total_distance[nextVertex] = total_distance[currentVertex] + edgeWeight
          parent[nextVertex] = currentVertex

    status[currentVertex] = True
    distance.pop(get_vertex_index(distance, currentVertex))

  print("================ RESULT ================")
  print("FROM INDEX", initialIndex)
  print("\ndistance: ", total_distance)
  print("\nparent: ", parent)

   


if __name__ == "__main__":
  graph = [
    [(0,1,5)],
    [(1,0,5), (1,2,2), (1,3,1), (1,4,3)],
    [(2,1,2)],
    [(3,1,1), (3,4,1), (3,5,2), (3,6,4)],
    [(4,1,3), (4,3,1)],
    [(5,3,2), (5,7,2)],
    [(6,3,4), (6,7,1)],
    [(7,5,2), (7,6,1), (7,8,1)],
    [(8,7,1)]
  ]

  dijkstra(graph, 1)  

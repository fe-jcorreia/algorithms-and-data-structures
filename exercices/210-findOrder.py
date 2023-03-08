
def topologicalSort(graph, initialVertex, status, courseSchedule):
  status[initialVertex] = 'D'

  for destiny in graph[initialVertex]:  
    if status[destiny] == 'U':
      canSort = topologicalSort(graph, destiny, status, courseSchedule)
      if not canSort: return False
    elif status[destiny] == 'D':
      return False
      
  status[initialVertex] = 'P'
  courseSchedule.append(initialVertex)
  return True

def findOrder(numCourses, prerequisites):
  status = ['U' for _ in range(numCourses)]
  graph = [[] for _ in range(numCourses)]
  for item in prerequisites:
    graph[item[1]].append(item[0])
  
  courseSchedule = []
  for i in range(numCourses):
    if status[i] == 'U':
      canSort = topologicalSort(graph, i, status, courseSchedule)
      if not canSort: return []
  courseSchedule.reverse()

  return courseSchedule  

print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(1, []))
print(findOrder(2, []))
print(findOrder(3, [[2,0],[2,1]]))
print(findOrder(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))
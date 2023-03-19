import heapq
  
def dfs(graph, initialVertex, itinerary, n):
  if len(itinerary) == n + 1:
    return True
  if initialVertex not in graph:
    return False

  while graph[initialVertex]:
    nextVertex = heapq.heappop(graph[initialVertex])
    itinerary.append(nextVertex)

    if dfs(graph, nextVertex, itinerary, n): return True
    heapq.heappush(graph[initialVertex], nextVertex)
    itinerary.pop()
  
  return False
    

def findItinerary(tickets):
  n = len(tickets)
  graph = {}
  for origin, destination in tickets:
    graph.setdefault(origin, [])
    heapq.heappush(graph[origin], destination)
  
  itinerary = ['JFK']
  initialVertex = 'JFK'

  dfs(graph, initialVertex, itinerary, n)

  return itinerary

def findItinerary(tickets):
  graph = {src: [] for src, dst in tickets}
  tickets = sorted(tickets)
  for src, dst in tickets:
    graph[src].append(dst)
  
  res = ['JFK']
  def dfs(src):
    if len(res) == len(tickets) + 1:
      return True
    if src not in graph:
      return False
    
    temp = list(graph[src])
    for i, v in enumerate(temp):
      graph[src].pop(i)
      res.append(v)
      if dfs(v): return True
      graph[src].insert(i, v)
      res.pop()
    return False
  
  dfs('JFK')
  return res


# print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# print(findItinerary([["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]]))
# print(findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))
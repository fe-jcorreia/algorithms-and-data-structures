from bfs import BreadthFirstSearch

class ConnectedComponents():
  def execute(self, graph):
    status = ['U' for _ in graph]
    connected_components = 0
    bfs = BreadthFirstSearch()

    for index, _ in enumerate(graph):
      if(status[index] == 'U'):
        connected_components += 1
        bfs.execute(graph, index, status)
    
    return connected_components


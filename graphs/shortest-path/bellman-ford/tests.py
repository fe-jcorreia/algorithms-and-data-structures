from bellmanFord import BellmanFord

class TestBellmanFord():
  def run_all_tests(self):
    self.test_small_graph()
    self.test_medium_graph()
    self.test_large_graph()
  
  def test_small_graph(self):
    graph = [
      [(0,1,2), (0,2,2)],
      [(1,0,2), (1,3,3)],
      [(2,0,2), (2,3,6), (2,4,4)],
      [(3,1,3), (3,2,6), (3,4,-5)],
      [(4,2,4), (4,3,-5)],
    ]

    bellmanFord = BellmanFord()
    bellmanFord.execute(graph, 0)

  def test_medium_graph(self):
    graph = [
      [(0,1,6), (0,2,5), (0,3,5)],
      [(1,4,-1)],
      [(2,1,-2), (2,4,1)],
      [(3,2,-2), (3,5,-1)],
      [(4,6,3)],
      [(5,6,3)],
      [],
    ]

    bellmanFord = BellmanFord()
    bellmanFord.execute(graph, 0)

  def test_large_graph(self):
    graph = [
      [(0,1,5), (0,2,2)],
      [(1,3,3), (1,4,7)],
      [(2,1,2), (2,5,9)],
      [(3,2,-2), (3,4,2), (3,5,6)],
      [(4,5,5), (4,6,-8), (4,7,7)],
      [(5,7,-2)],
      [(6,8,4)],
      [(7,6,3)],
      [],
    ]

    bellmanFord = BellmanFord()
    bellmanFord.execute(graph, 0)

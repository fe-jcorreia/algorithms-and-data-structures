from kosaraju import Kosaraju

class TestKosaraju():
  def run_all_tests(self):
    self.test_small_graph()
    self.test_medium_graph()
    self.test_large_graph()
    self.test_second_large_graph()
  
  def test_small_graph(self):
    graph = [
      [(0,2,5), (0,3,4)],
      [(1,0,3)],
      [(2,1,3)],
      [(3,4,7)],
      [],
    ]

    kosaraju = Kosaraju()
    stronglyConnectedComponents = kosaraju.execute(graph)

    print(f"Small graph kosaraju check: {stronglyConnectedComponents}")

  def test_medium_graph(self):
    graph = [
      [(0,1,5)],
      [(1,2,2)],
      [(2,3,2), (2,4,2)],
      [(3,0,1)],
      [(4,5,3)],
      [(5,6,2)],
      [(6,4,1), (6,7,1)],
      [],
    ]

    kosaraju = Kosaraju()
    stronglyConnectedComponents = kosaraju.execute(graph)

    print(f"Medium graph kosaraju check: {stronglyConnectedComponents}")

  def test_large_graph(self):
    graph = [
      [(0,1,2)],
      [(1,2,4), (1,3,4)],
      [(2,0,9)],
      [(3,4,5)],
      [(4,5,6)],
      [(5,3,5)],
      [(6,5,3), (6,7,2)],
      [(7,8,6)],
      [(8,9,3)],
      [(9,6,4), (9,10,2)],
      [],
    ]

    kosaraju = Kosaraju()
    stronglyConnectedComponents = kosaraju.execute(graph)

    print(f"Large graph kosaraju check: {stronglyConnectedComponents}")
  
  def test_second_large_graph(self):
    graph = [
      [(0,1,2), (0,2,4), (0,9,3)],
      [(1,2,3), (1,10,3)],
      [(2,4,6)],
      [(3,6,5), (3,9,8)],
      [(4,0,3)],
      [(5,3,4), (5,8,2)],
      [(6,10,3)],
      [(7,5,6)],
      [(8,0,4), (8,4,3), (8,7,4)],
      [(9,6,1)],
      [(10,9,2)],
    ]

    kosaraju = Kosaraju()
    stronglyConnectedComponents = kosaraju.execute(graph)

    print(f"Large graph kosaraju check: {stronglyConnectedComponents}")

from connectedComponents import ConnectedComponents

class TestConnectedComponents():
  def run_all_tests(self):
    self.test_small_graph()
    self.test_medium_graph()
    self.test_large_graph()
  
  def test_small_graph(self):
    graph = [
      [(0,1,5), (0,2,3)],
      [(1,0,5), (1,2,1), (1,4,6)],
      [(2,0,3), (2,1,1), (2,3,7)],
      [(3,2,7)],
      [(4,1,6)],
    ]

    connectedComponents = ConnectedComponents()
    c = connectedComponents.execute(graph)
    assert c == 1
    print(f"Small graph: OK - Connected Components: {c}")


  def test_medium_graph(self):
    graph = [
      [(0,1,5)],
      [(1,0,5), (1,2,2), (1,4,3)],
      [(2,1,2)],
      [(3,5,2), (3,6,4)],
      [(4,1,3)],
      [(5,3,2)],
      [(6,3,4)],
      [(7,8,1)],
      [(8,7,1)],
    ]

    connectedComponents = ConnectedComponents()
    c = connectedComponents.execute(graph)
    assert c == 3
    print(f"Medium graph: OK - Connected Components: {c}")

  def test_large_graph(self):
    graph = [
      [(0,1,3), (0,4,12), (0,12,1)],
      [(1,0,3), (1,3,2), (1,12,5)],
      [(2,6,5), (2,7,10), (2,13,2), (2,14,13)],
      [(3,1,2), (3,4,3)],
      [(4,0,12), (4,3,3), (4,12,1)],
      [(5,8,6), (5,9,1), (5,10,14)],
      [(6,2,5), (6,7,1)],
      [(7,2,10), (7,6,1), (7,14,4)],
      [(8,5,6), (8,9,3)],
      [(9,5,1), (9,8,3), (9,10,5)],
      [(10,5,14), (10,9,5)],
      [],
      [(12,0,1), (12,1,5), (12,4,1)],
      [(13,2,2), (13,14,3)],
      [(14,2,13), (14,7,4), (14,13,3)]
    ]

    connectedComponents = ConnectedComponents()
    c = connectedComponents.execute(graph)
    assert c == 4
    print(f"Large graph: OK - Connected Components: {c}")

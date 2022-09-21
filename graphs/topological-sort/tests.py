from topologicalSort import TopologicalSort

class TestTopologicalSort():
  def run_all_tests(self):
    self.test_check_cicle()
    self.test_small_graph()
    self.test_medium_graph()
    self.test_large_graph()
  
  def test_check_cicle(self):
    graph = [
      [(0,1,5), (0,2,3), (0,3,4)],
      [(1,3,5)],
      [(2,3,3)],
      [(3,0,2)],
    ]

    topologicalSort = TopologicalSort()
    finalSort = topologicalSort.execute(graph)
    assert finalSort == None

    print("Cicle Topological Sort OK:", finalSort)

  def test_small_graph(self):
    graph = [
      [(0,1,5), (0,2,3), (0,3,4)],
      [(1,3,5)],
      [(2,3,3)],
      [],
    ]

    topologicalSort = TopologicalSort()
    finalSort = topologicalSort.execute(graph)
    assert finalSort == [0, 2, 1, 3]

    print("Small Topological Sort OK:", finalSort)

  def test_medium_graph(self):
    graph = [
      [(0,1,5), (0,6,4)],
      [(1,2,2), (1,3,1)],
      [(2,3,2), (2,4,5)],
      [(3,5,1)],
      [],
      [(5,4,2)],
      [(6,5,1)],
    ]

    topologicalSort = TopologicalSort()
    finalSort = topologicalSort.execute(graph)
    assert finalSort == [0, 6, 1, 2, 3, 5, 4]

    print("Medium Topological Sort OK:", finalSort)

  def test_large_graph(self):
    graph = [
      [(0,1,3), (0,2,12)],
      [(1,3,2)],
      [(2,3,13)],
      [(3,4,2), (3,5,3), (3,6,6)],
      [(4,5,1)],
      [],
      [(6,7,5), (6,9,1)],
      [(7,8,4)],
      [(8,9,3)],
      [(9,10,5)],
      [],
    ]

    topologicalSort = TopologicalSort()
    finalSort = topologicalSort.execute(graph)
    assert finalSort == [0, 2, 1, 3, 6, 7, 8, 9, 10, 4, 5]

    print("Large Topological Sort OK:", finalSort)

from opcode import hascompare
from checkCicle import CheckCicle

class TestCheckCicle():
  def run_all_tests(self):
    self.test_small_graph()
    self.test_medium_graph()
    self.test_large_graph()
  
  def test_small_graph(self):
    graph = [
      [(0,1,5), (0,2,3)],
      [(1,0,5), (1,4,6)],
      [(2,0,3), (2,3,7)],
      [(3,2,7)],
      [(4,1,6)],
    ]

    checkCicle = CheckCicle()
    hasCicle = checkCicle.execute(graph)
    assert hasCicle == False

    print(f"Small graph cicle check: {hasCicle}")

  def test_medium_graph(self):
    graph = [
      [(0,1,5)],
      [(1,0,5), (1,2,2), (1,3,1), (1,4,3)],
      [(2,1,2)],
      [(3,1,1)],
      [(4,1,3)],
      [(5,7,2)],
      [(6,7,1)],
      [(7,5,2), (7,6,1), (7,8,1)],
      [(8,7,1)],
    ]

    checkCicle = CheckCicle()
    hasCicle = checkCicle.execute(graph)
    assert hasCicle == False

    print(f"Medium graph cicle check: {hasCicle}")

  def test_large_graph(self):
    graph = [
      [(0,1,3), (0,4,12), (0,12,1), (0,13,6)],
      [(1,0,3), (1,3,2), (1,12,5)],
      [(2,6,5), (2,7,10), (2,13,2), (2,14,13)],
      [(3,1,2), (3,4,3), (3,6,1)],
      [(4,0,12), (4,3,3), (4,10,2), (4,12,1)],
      [(5,8,6), (5,9,1), (5,10,14)],
      [(6,2,5), (6,3,1), (6,7,1), (6,8,2)],
      [(7,2,10), (7,6,1), (7,14,4)],
      [(8,5,6), (8,6,2), (8,9,3)],
      [(9,5,1), (9,8,3), (9,10,5)],
      [(10,4,2), (10,5,14), (10,9,5), (10,11,1)],
      [(11,10,1), (11,12,5)],
      [(12,0,1), (12,1,5), (12,4,1), (12,11,5)],
      [(13,0,6), (13,2,2), (13,14,3)],
      [(14,2,13), (14,7,4), (14,13,3)]
    ]

    checkCicle = CheckCicle()
    hasCicle = checkCicle.execute(graph)
    assert hasCicle == True

    print(f"Large graph cicle check: {hasCicle}")

from knapsack import Knapsack

class TestKnapsack():
  def run_all_tests(self):
    self.test_small_array()
    self.test_medium_array()
    self.test_large_array()

  def test_small_array(self):
    wt = [1, 3, 4, 5]
    value = [1, 4, 5, 7]

    knapsack = Knapsack()
    total_value, weights = knapsack.execute(wt, value, 7)
    assert total_value == 9
    assert weights == [4, 3]

    print("Small Knapsack OK")

  def test_medium_array(self):
    wt = [4, 5, 1, 3, 2, 5]
    value = [2, 3, 1, 5, 4, 7]

    knapsack = Knapsack()
    total_value, weights = knapsack.execute(wt, value, 15)
    assert total_value == 19
    assert weights == [5, 2, 3, 5]

    print("Medium Knapsack OK")

  def test_large_array(self):
    wt = [92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58]
    value = [44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63]

    knapsack = Knapsack()
    total_value, weights = knapsack.execute(wt, value, 878)
    assert total_value == 1024
    assert weights == [58, 14, 70, 25, 56, 18, 32, 44, 6, 82, 92, 68, 84, 83, 43, 4, 92]

    print("Large Knapsack OK")
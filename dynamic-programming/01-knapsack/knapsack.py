class Knapsack():
  def get_weights(self, wt, maxWeight, total_value):
    i = len(wt)
    j = maxWeight
    check_value = total_value[i][j]
    weights = []
    while check_value != 0:
      if total_value[i - 1][j] == check_value:
        i -= 1
        check_value = total_value[i][j]
        continue
      else:
        current_weight = wt[i - 1]
        weights.append(current_weight)
        i -= 1
        j -= current_weight
        check_value = total_value[i][j]
    
    print("weights: ", weights)
    return weights

  def execute(self, wt, value, maxWeight): 
    total_value = [[0 for _ in range(maxWeight + 1)] for _ in range(len(wt) + 1) ]

    for i in range(len(wt) + 1):
      for w in range(maxWeight + 1):
        if i == 0 or w == 0:
          total_value[i][w] = 0
        elif wt[i - 1] <= w:
          total_value[i][w] = max(value[i - 1] + total_value[i - 1][w - wt[i - 1]], total_value[i - 1][w])
        else:
          total_value[i][w] = total_value[i - 1][w]
  
    for item in total_value:
      print(item)

    weights = self.get_weights(wt, maxWeight, total_value)
    
    return total_value[len(wt)][maxWeight], weights

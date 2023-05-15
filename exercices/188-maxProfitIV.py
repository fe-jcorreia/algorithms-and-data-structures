def maxProfit(k, prices):
  buy = [float('-inf')] * (k + 1)
  sell = [0] * (k + 1)

  for price in prices:
    for i in range(1, k + 1):
      buy[i] = max(buy[i], sell[i - 1] - price)
      sell[i] = max(sell[i], buy[i] + price)
  
  return sell[-1]

print(maxProfit(2, [2,4,1]))
print(maxProfit(2, [3,2,6,5,0,3]))
print(maxProfit(3, [3,2,6,5,0,3]))
print(maxProfit(2, [3,3,5,0,0,3,1,4]))
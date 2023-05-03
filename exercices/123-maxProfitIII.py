def maxProfit(prices):
  if not prices:
    return 0

  buy1, buy2 = float('inf'), float('inf')
  sell1, sell2 = 0, 0

  for price in prices:
    buy1 = min(buy1, price)
    sell1 = max(sell1, price - buy1)

    buy2 = min(buy2, price - sell1)
    sell2 = max(sell2, price - buy2)

  return sell2


print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1,2,4,2,5,7,2,4,9,0]))

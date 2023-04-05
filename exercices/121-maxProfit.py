def maxProfit_n2(prices):
  profit = 0
  n = len(prices)
  
  for i, p in enumerate(prices):
    if i == n - 1: continue
    profit = max(profit, max(prices[i + 1:]) - p)    

  return profit

def maxProfit_arr(prices):
  n = len(prices)
  dayProfits = [0] * n

  for i in range(n - 2, -1, -1):
    dayProfits[i] = max(prices[i + 1] - prices[i], 
                        dayProfits[i + 1] + prices[i + 1] - prices[i])

  return max(dayProfits)

def maxProfit_2poiters(prices):
  l, r = 0, 1
  maxP = 0

  while r < len(prices):
    if prices[l] < prices[r]:
      profit = prices[r] - prices[l]
      maxP = max(maxP, profit)
    else:
      l = r
    r += 1
  
  return maxP

def maxProfit(prices):
  n = len(prices)
  nextDayProfit = 0
  maxP = 0

  for i in range(n - 2, -1, -1):
    profit = max(prices[i + 1] - prices[i], nextDayProfit + prices[i + 1] - prices[i])
    maxP = max(maxP, profit)
    nextDayProfit = profit

  return maxP

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

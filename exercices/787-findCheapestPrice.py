import sys

def findCheapestPrice(n, flights, src, dst, k):
  prices = [sys.maxsize] * n
  prices[src] = 0

  for _ in range(k + 1):
    tmpPrices = prices.copy()

    for s, d, p in flights:
      if prices[s] == sys.maxsize:
        continue
      if tmpPrices[d] > prices[s] + p:
        tmpPrices[d] = prices[s] + p

    prices = tmpPrices
  
  return prices[dst] if prices[dst] != sys.maxsize else -1

def findCheapestPrice_(n, flights, src, dst, k): # bellman-ford
  totalPrice = [sys.maxsize] * n
  totalPrice[src] = 0

  for _ in range(n - 1):
    for s, d, p in flights:
      if totalPrice[d] > totalPrice[s] + p:
        totalPrice[d] = totalPrice[s] + p

  for s, d, p in flights:
      if totalPrice[d] > totalPrice[s] + p: return -1
  
  return totalPrice

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
print(findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))
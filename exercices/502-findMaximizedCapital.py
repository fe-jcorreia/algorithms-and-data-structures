import heapq

def findMaximizedCapital(k, w, profits, capital):
  cash = w
  maxProfit = []
  minCapital = []

  for i in range(len(profits)):
    heapq.heappush(minCapital, (capital[i], -profits[i]))

  for _ in range(k):

    while minCapital and minCapital[0][0] <= cash:
      _, profit = heapq.heappop(minCapital)
      heapq.heappush(maxProfit, profit)

    if not maxProfit:
      return cash

    cash += -heapq.heappop(maxProfit)
  
  return cash
  

print(findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
# print(findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))
print(findMaximizedCapital(2, 0, [4999,5000,3], [0,0,1]))
# print(findMaximizedCapital(1, 0, [1,2,3], [1,1,2]))
# print(findMaximizedCapital(10, 0, [1,2,3], [0,1,2]))





def findMaximizedCapital_old(k, w, profits, capital):
  cash = w
  heap = []

  for i in range(len(profits)):
    heapq.heappush(heap, (-profits[i], capital[i]))

  for _ in range(k):
    if len(heap) == 0:
      return cash
    
    cantAfford = []
    profit, cost  = heapq.heappop(heap)

    while cost > cash:
      if len(heap) == 0:
        return cash
      cantAfford.append((profit, cost))
      profit, cost = heapq.heappop(heap)
    
    cash += -profit
    for item in cantAfford:
      heapq.heappush(heap, item)
  
  return cash

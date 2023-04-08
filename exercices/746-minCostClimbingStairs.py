def minCostClimbingStairs(cost):
  n = len(cost)
  if n <= 1: return 0

  next1 = cost[-2]
  next2 = cost[-1]
  for i in range(n - 3, -1, -1):
    minCost = cost[i] + min(next1, next2)
    next2 = next1
    next1 = minCost
  
  return min(next1, next2)

print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
def maxCoins_old(nums):
  cache = {}
  
  def dfs(arr):
    if len(arr) == 0: return 0
    
    if tuple(arr) in cache: return cache[tuple(arr)]
    
    maxProfit = 0
    for i in range(len(arr)):
      before = 1 if i - 1 < 0 else arr[i - 1]
      after = 1 if i + 1 > len(arr) - 1 else arr[i + 1]
      
      currProfit = before * arr[i] * after
      restProfit = dfs(arr[:i] + arr[i + 1:])
      maxProfit = max(maxProfit, currProfit + restProfit)

    cache[tuple(arr)] = maxProfit
    return maxProfit

  return dfs(nums)

def maxCoins(nums):
  nums = [1] + nums + [1]
  cache = {}

  def dfs(l, r):
    if l > r: return 0
    if (l, r) in cache: return cache[(l, r)]

    cache[(l, r)] = 0
    for i in range(l, r + 1):
      currProfit = nums[l - 1] * nums[i] * nums[r + 1]
      currProfit += dfs(l, i - 1) + dfs(i + 1, r)
      cache[(l, r)] = max(cache[(l, r)], currProfit) 
  
    return cache[(l, r)]

  return dfs(1, len(nums) - 2)

print(maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]))
print(maxCoins([7,9,8,0,7,1,3,5,5,2,3]))
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))

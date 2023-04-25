def numSquares(n):
  dp = [0, 1]

  perfSq = []
  p = 1
  while p * p <= n:
    perfSq.append(p * p)
    p += 1 

  for i in range(2, n + 1):
    dp.append(float('inf'))
    for sq in perfSq:
      if sq > i: break
      dp[i] = min(dp[i], 1 + dp[i - sq])
  
  return dp[-1] 

def numSquares_old(self, n: int) -> int:
  def isPerfectSquare(x):
    y=int(x ** 0.5)
    return y * y == x
  
  def isFourSquare(x):
    while x % 4 == 0:
      x /= 4
    return x % 8 == 7
  
  if isPerfectSquare(n):
    return 1
  
  if isFourSquare(n):
    return 4
  
  i = 1
  while i * i <= n:
    y = n - i * i
    if isPerfectSquare(y):
      return 2
    i += 1
  
  return 3

print(numSquares(4))  
print(numSquares(12))
print(numSquares(13))
def knapsack(w, n, val, wt):
  dp = [[0] * (w + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, w + 1):
      if j >= wt[i - 1]:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
      else:
        dp[i][j] = dp[i - 1][j]
      
  items = [0] * n
  col = w
  row = n
  while col != 0 and row - 1 >= 0:
    if dp[row][col] != dp[row - 1][col]:
      items[row - 1] = 1
      col -= wt[row - 1]
    row -= 1

  return (dp[n][w], items)

ans = knapsack(10, 4, [10, 40, 30, 50], [5, 4, 6, 3])
print(ans)
ans = knapsack(8, 4, [1, 2, 5, 6], [2, 3, 4, 5])
print(ans)
ans = knapsack(4, 3, [1, 2, 3], [4, 5, 1])
print(ans)
ans = knapsack(3, 3, [1, 2, 3], [4, 5, 6])
print(ans)
ans = knapsack(50, 3, [60, 100, 120], [10, 20, 30])
print(ans)
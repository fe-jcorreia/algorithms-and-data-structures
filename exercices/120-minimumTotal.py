def minimumTotal(triangle):
  n = len(triangle)
  tri = [0] * (n + 1)

  for i in range(n - 1, -1, -1):
    for j in range(i + 1):
      tri[j] = triangle[i][j] + min(tri[j], tri[j + 1])

  return tri[0]

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minimumTotal([[-10]]))


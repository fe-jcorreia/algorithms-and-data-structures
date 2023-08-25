def grayCode(n):
  res = [0]
  for i in range(n):
    for j in range(len(res) - 1, -1, -1):
      res.append(res[j] | (1 << i))
  return res


print(grayCode(1))
print(grayCode(2))
print(grayCode(3))
print(grayCode(4))
print(grayCode(5))

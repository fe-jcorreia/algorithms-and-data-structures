def nthUglyNumber(n): # 14
  result = [1]
  p2 = p3 = p5 = 0
  for _ in range(1, n):
    a = result[p2] * 2
    b = result[p3] * 3
    c = result[p5] * 5
    m = min(a, b, c)
    result.append(m)

    if m == a:
      p2 += 1
    if m == b:
      p3 += 1
    if m == c:
      p5 += 1

  return result[-1]
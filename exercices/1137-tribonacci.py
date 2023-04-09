def tribonacci(n):
  t0 = 0
  t1 = 1
  t2 = 1
  
  if n == 0: return 0
  if n == 1 or n == 2: return 1

  for _ in range(3, n + 1):
    trib = t0 + t1 + t2
    t0 = t1
    t1 = t2
    t2 = trib

  return t2

print('n = 0:', tribonacci(0))
print('n = 1:', tribonacci(1))
print('n = 2:', tribonacci(2))
print('n = 3:', tribonacci(3))
print('n = 4:', tribonacci(4))
print('n = 5:', tribonacci(5))
print('n = 6:', tribonacci(6))
print('n = 7:', tribonacci(7))
print('n = 8:', tribonacci(8))
print('n = 25:', tribonacci(25))
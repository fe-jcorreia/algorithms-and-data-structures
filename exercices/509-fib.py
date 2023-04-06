def fib(n):
  if n == 0: return 0
  if n == 1: return 1

  fibMinus1 = 1
  fibMinus2 = 0
  currFib = 0

  for _ in range(2, n + 1):
    currFib = fibMinus1 + fibMinus2
    fibMinus2 = fibMinus1
    fibMinus1 = currFib
  
  return fibMinus1

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
def fact(n):
  if n == 1 or n == 0:
    return 1

  return n * fact(n - 1)
  
def numTrees(n):
  return int((fact(2*n))/(fact(n) * fact(n) * (n+1)))

def numTrees_DP(n):
  f = []
  for i in range(n + 1): 
    if i == 0 or i == 1:
      f.append(1)
      continue

    f.append(0)
    for j in range(i):
      f[i] += f[j] * f[i - 1 - j] 
    
  return f[n]

print(numTrees(1))
print(numTrees(2))
print(numTrees(3))
print(numTrees(4))
print(numTrees(5))

print(numTrees_DP(1))
print(numTrees_DP(2))
print(numTrees_DP(3))
print(numTrees_DP(4))
print(numTrees_DP(5))
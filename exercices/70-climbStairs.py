def climbStairs_old(n):
  if n == 0: return 1
  if n < 0: return 0
  
  possibilities = 0
  possibilities += climbStairs_old(n - 1)
  possibilities += climbStairs_old(n - 2)

  return possibilities

def climbStairs_mem(n):
  pos = [1]

  def solve(n):
    if n < 0: return 0
    if len(pos) - 1 >= n: return pos[n]
    
    possibilities = 0
    possibilities += solve(n - 1)
    possibilities += solve(n - 2)

    pos.append(possibilities)
    return possibilities
  
  return solve(n)

def climbStairs_dp(n):
  pos = [1, 1]

  for step in range(2, n + 1):
    pos.append(pos[step - 1] + pos[step - 2])

  return pos[n]

def climbStairs(n):
  step1 = 1
  step2 = 1

  for _ in range(2, n + 1):
    aux = step1
    step1 = step1 + step2 
    step2 = aux
  
  return step1 


print(climbStairs(1)) # 1
print(climbStairs(2)) # 2
print(climbStairs(3)) # 3
print(climbStairs(4)) # 5
print(climbStairs(5)) # 8

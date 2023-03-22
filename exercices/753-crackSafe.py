ans = None

def crackSafe(n, k):
  global ans
  visited = set()
  def backtrack(curr):
    global ans
    if len(visited) == k**n:
      ans = curr
      return True
    
    for i in range(k):
      new_curr = str(i) + curr
      if new_curr[:n] not in visited:
        visited.add(new_curr[:n])
        if backtrack(new_curr):
          return True
        visited.remove(new_curr[:n])
    
    return False
  
  backtrack('0' * (n-1))
  return ans

print(crackSafe(1,2))
print(crackSafe(2,2))

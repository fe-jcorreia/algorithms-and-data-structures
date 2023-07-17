def makesquare(matchsticks):
  squareSide = sum(matchsticks) // 4
  if sum(matchsticks) / 4 != squareSide: return False
  matchsticks = sorted(matchsticks, reverse=True)

  sides = [0] * 4
  
  def dfs(index):
    if index == len(matchsticks):
      return True
    
    for i in range(4):
      if sides[i] + matchsticks[index] <= squareSide:
        sides[i] += matchsticks[index]
        if dfs(index + 1): return True
        sides[i] -= matchsticks[index]
    
    return False
  
  return dfs(0)
  

    




print(makesquare([1,1,2,2,2]))
print(makesquare([3,3,3,3,4]))
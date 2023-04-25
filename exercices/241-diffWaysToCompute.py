def diffWaysToCompute(expression):
  def backtrack(s):
    if s.isnumeric():
      return [int(s)]
    
    res = []
    for i, char in enumerate(s):
      if char in ['+', '-', '*']:
        left = backtrack(s[:i])
        right = backtrack(s[i+1:])
          
        for l in left:
          for r in right:
            res.append(eval(str(l) + char + str(r)))
            
    return res

  return backtrack(expression)

# print(diffWaysToCompute("2-1-1"))
print(diffWaysToCompute("2*3-4*5"))
def generateParenthesis(n):
  stack = []
  res = []

  def backtrack(openPar, closePar):
    if openPar == closePar == n:
      res.append(''.join(stack))
      return
    
    if openPar < n:
      stack.append('(')
      backtrack(openPar + 1, closePar)
      stack.pop()
    
    if closePar < openPar:
      stack.append(')')
      backtrack(openPar, closePar + 1)
      stack.pop()

  backtrack(0, 0)

  return res
  


print(generateParenthesis(1))
print(generateParenthesis(2))
print(generateParenthesis(3))
# print(generateParenthesis(4))
# print(generateParenthesis(5))
# print(generateParenthesis(6))
# print(generateParenthesis(7))
# print(generateParenthesis(8))
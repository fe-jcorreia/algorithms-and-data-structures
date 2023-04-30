def maximalRectangle(matrix):
  if not matrix:
    return 0
  
  n = len(matrix[0])
  heights = [0] * (n + 1)
  maxArea = 0

  for row in matrix:
    for i in range(n):
      heights[i] = heights[i] + 1 if row[i] == "1" else 0
    
    stack = [-1]
    for i in range(n + 1):
      while heights[i] < heights[stack[-1]]:
        h = heights[stack.pop()]
        w = i - stack[-1] - 1
        maxArea = max(maxArea, h * w)
        
      stack.append(i)
  
  return maxArea

print(maximalRectangle([["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]))
print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalRectangle([["0"]]))
print(maximalRectangle([["1"]]))
def maxArea(height):
  maxArea = 0

  for i, x in enumerate(height):
    for j, y in enumerate(height[i + 1:]):
      if maxArea < (j + 1) * min(x, y):
        maxArea = (j + 1) * min(x, y)
  
  return maxArea

def maxArea_opt(height):
  maxArea = 0
  l = 0
  r = len(height) - 1

  while r != l:
    if maxArea < (r - l) * min(height[r], height[l]):
      maxArea = (r - l) * min(height[r], height[l])
    
    if height[l] <= height[r]:
      l += 1
    else:
      r -= 1
  
  return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))

print(maxArea_opt([1,8,6,2,5,4,8,3,7]))
print(maxArea_opt([1,1]))
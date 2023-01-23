def trap(height):
  current = 0
  maxWater = 0
  stack =   []

  while current < len(height): 
    while stack and height[current] > height[stack[-1]]:
      top = stack[-1]
      stack.pop()

      if not stack:
        break

      distance = current - stack[-1] - 1
      bounded_height = min(height[current], height[stack[-1]]) - height[top]

      maxWater += distance * bounded_height

    stack.append(current)
    current += 1
  
  return maxWater

def trap_opt(height):
  left = 0
  right = len(height) - 1
  left_max = right_max = 0
  maxWater = 0

  while left < right:
    if height[left] < height[right]:
      if height[left] >= left_max:
        left_max = height[left]
      else:
        maxWater += left_max - height[left]
      left += 1
    else:
      if height[right] >= right_max:
        right_max = height[right]
      else:
        maxWater += right_max - height[right]
      right -= 1 

  return maxWater

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6

print(trap_opt([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
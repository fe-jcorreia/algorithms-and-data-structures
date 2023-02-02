def mySqrt(x):
  lowest = 0
  highest = x

  if x == 1:
    return 1

  while lowest < highest - 1:
    mid = (lowest + highest) // 2

    if (mid * mid) > x:
      highest = mid
    elif (mid * mid) < x:
      lowest = mid
    else:
      return mid
    
  return lowest 
    
print(mySqrt(4)) # 2
print(mySqrt(8)) # 2
print(mySqrt(9)) # 3
print(mySqrt(19)) # 4
print(mySqrt(49)) # 7
print(mySqrt(1)) # 1
print(mySqrt(0)) # 0
print(mySqrt(2)) # 1

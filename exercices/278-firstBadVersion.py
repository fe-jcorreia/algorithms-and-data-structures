def isBadVersion(x):
  if x >= 15:
    return True

  return False

def firstBadVersion(n):
  lowest = 1
  highest = n
  
  if isBadVersion(lowest):
    return lowest

  while lowest < highest - 1:
    mid = (highest + lowest) // 2

    if isBadVersion(mid):
      highest = mid
    else:
      lowest = mid
    
  return highest

print(firstBadVersion(20)) # 4
# [1  2  3  4  5]
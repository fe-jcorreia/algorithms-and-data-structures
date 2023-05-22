import heapq

def findClosestElements_old(arr, k, x):
  heap = []
  ans = []

  for num in arr: heapq.heappush(heap, (abs(num - x), num))
  for _ in range(k): 
    _, num = heapq.heappop(heap)
    ans.append(num)
  
  return sorted(ans)

def findClosestElements(arr, k, x):
  if x > arr[-1]: return arr[-k:]
  if x < arr[0]: return arr[:k]

  def binSearch(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
      mid = (l + r) // 2
      if target > arr[mid]:
        l = mid + 1
      elif target < arr[mid]:
        r = mid - 1
      else:
        return mid
    return min(r, l, key=lambda i: (abs(x - arr[i])))


  indexStart = binSearch(arr, x)

  length = 1
  l = r = indexStart
  while length < k:
    if l == 0: r += 1
    elif r == len(arr) - 1: l -= 1
    else:
      if abs(x - arr[r + 1]) >= abs(x - arr[l - 1]):
        l -= 1
      else:
        r += 1
    length += 1
    
  return arr[l:r + 1]


print(findClosestElements([1,2,3,4,5], 4, 3))
print(findClosestElements([1,2,3,4,5], 4, -1))
print(findClosestElements([1,1,1,10,10,10], 1, 9))
print(findClosestElements([-2,-1,1,2,3,4,5], 7, 3))
print(findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))

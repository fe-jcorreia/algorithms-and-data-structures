def binarySearch(nums, target):
  l = 0
  r = len(nums)
  
  while l <= r:
    mid = (l + r) // 2

    if target > nums[mid]:
      l = mid + 1
    elif target < nums[mid]:
      r = mid - 1
    else:
      return mid
  
  return 

def maxEnvelopes(envelopes):
  sortedEnvelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
  lis = []

  for (w, h) in sortedEnvelopes:
    if not lis or h > lis[-1]:
      lis.append(h)
    else:
      l, r = 0, len(lis)
      while l < r:
        m = (l + r) // 2
        if lis[m] < h:
          l = m + 1
        else:
          r = m

      lis[l] = h

  return len(lis)

print(maxEnvelopes([[5,4],[6,7],[6,4],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print(maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))

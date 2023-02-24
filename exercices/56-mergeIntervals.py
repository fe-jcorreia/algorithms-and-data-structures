def merge(intervals):
  intervals = sorted(intervals, key= lambda i : i[0])
  res = [intervals[0]]

  for start, end in intervals[1:]:
    currentEnd = res[-1][1]

    if start <= currentEnd:
      res[-1][1] = max(currentEnd, end)
    else:
      res.append([start, end])
  
  return res

print(merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]])) # [[1,5]]
print(merge([[1,4],[0,4]])) # [[0,4]]
print(merge([[1,4],[0,0]])) # [[0,0],[1,4]]
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [[1,10]]
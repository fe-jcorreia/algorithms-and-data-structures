import heapq

def largestInteger(num):
  odd = []
  even = []
  nums = list(str(num))
  ans = []

  for num in nums:
    if int(num) % 2 == 0:
      heapq.heappush(even, -int(num))
    else:
      heapq.heappush(odd, -int(num))

  for num in nums:
    if int(num) % 2 == 0:
      ans.append(str(-heapq.heappop(even)))
    else:
      ans.append(str(-heapq.heappop(odd)))

  return int("".join(ans))

print(largestInteger(1234))
print(largestInteger(65875))

import heapq

def maxSubsequence(nums, k):
  heap = []
  ans = []

  for i, num in enumerate(nums): heapq.heappush(heap, (-num, i))
  for _ in range(k): ans.append(heapq.heappop(heap))
  ans = sorted(ans, key=lambda x: x[1])
  for i in range(k): ans[i] = -ans[i][0]

  return ans


print(maxSubsequence([2,1,3,3], 2))
print(maxSubsequence([-1,-2,3,4], 3))
print(maxSubsequence([3,4,3,3], 2))

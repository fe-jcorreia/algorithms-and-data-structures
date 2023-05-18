import heapq

def kSmallestPairs(nums1, nums2, k):
  heap = [(nums1[0] + nums2[0], nums1[0], nums2[0], 0, 0)]
  visited = set((0, 0))
  ans = []

  while heap and len(ans) < k:
    _, a, b, i, j = heapq.heappop(heap)
    ans.append([a, b])

    if i < len(nums1) - 1 and (i + 1, j) not in visited:
      heapq.heappush(heap, (nums1[i + 1] + nums2[j], nums1[i + 1], nums2[j], i + 1, j))
      visited.add((i + 1, j))
    
    if j < len(nums2) - 1 and (i, j + 1) not in visited:
      heapq.heappush(heap, (nums1[i] + nums2[j + 1], nums1[i], nums2[j + 1], i, j + 1))
      visited.add((i, j + 1))
  
  return ans

print(kSmallestPairs([1,7,11], [2,4,6], 3))
print(kSmallestPairs([1,1,2], [1,2,3], 2))
print(kSmallestPairs([1,2], [3], 3))
print(kSmallestPairs([1,1,2], [1,2,3], 10))
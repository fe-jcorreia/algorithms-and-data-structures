import heapq

def frequencySort(s):
  heap = []
  charCount = {}
  ans = []

  for char in s:
    charCount[char] = 1 + charCount.get(char, 0)
  
  for char in charCount:
    heapq.heappush(heap, (-charCount[char], char))
  
  while heap:
    count, char = heapq.heappop(heap)

    for _ in range(-count):
      ans.append(char)
  
  return "".join(ans)

print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))

import heapq

def topKFrequent(words, k):
  freq = {}
  heap = []
  ans = []

  for word in words: freq[word] = 1 + freq.get(word, 0)
  
  for key, value in freq.items():
    heapq.heappush(heap, (-value, key))
  for _ in range(k):
    _, word = heapq.heappop(heap)
    ans.append(word)
  
  return ans


print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))
print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))

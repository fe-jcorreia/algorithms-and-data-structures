def topKFrequent(nums, k):
  freq = {}
  count = [[] for _ in range(len(nums) + 1)]

  for num in nums:
      freq[num] = 1 + freq.get(num, 0)
    
  for num in freq:
    count[freq[num]].append(num)

  res = []
  for i in range(len(count) - 1, 0, -1):
    for n in count[i]:
      res.append(n)
      if len(res) == k:
        return res
  
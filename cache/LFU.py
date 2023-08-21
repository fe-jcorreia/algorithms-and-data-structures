from collections import OrderedDict, defaultdict

class LFUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.freq = {}
    self.cache = defaultdict(lambda: OrderedDict())
    self.minFreq = 1

  def get(self, key: int) -> int:
    if key in self.freq:
      f = self.freq[key]
      self.cache[f + 1][key] = self.cache[f].pop(key)
      self.freq[key] = f + 1

      if self.minFreq == f and not len(self.cache[f]):
        self.minFreq = f + 1
      
      return self.cache[f + 1][key]

    return -1

  def put(self, key: int, value: int) -> None:
    hasKey = self.get(key) != -1

    if hasKey:
      f = self.freq[key]
      self.cache[f][key] = value
    else:
      if len(self.freq) >= self.capacity:
        k, _ = self.cache[self.minFreq].popitem(last=False)
        del self.freq[k]

      self.minFreq = 1
      self.freq[key] = 1
      self.cache[1][key] = value


result = []
obj = LFUCache(2)
result.append(obj.put(1,1))
result.append(obj.put(2,2))
result.append(obj.get(1))
result.append(obj.put(3,3))
result.append(obj.get(2))
result.append(obj.get(3))
result.append(obj.put(4,4))
result.append(obj.get(1))
result.append(obj.get(3))
result.append(obj.get(4))

print(result)
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = OrderedDict()

    def get(self, key: int) -> int:
      if key in self.cache:
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]
      else:
        return -1

    def put(self, key: int, value: int) -> None:
      if key in self.cache:
        self.cache.pop(key)
        self.cache[key] = value
      else:
        if len(self.cache) < self.capacity:
          self.cache[key] = value
        else:
          self.cache.popitem(last=False)
          self.cache[key] = value 


obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

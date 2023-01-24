class RecentCounter:
    def __init__(self):
      self.queue = []

    def ping(self, t: int) -> int:
      if not self.queue:
        self.queue.append(t)
        return len(self.queue)
      
      while self.queue and self.queue[0] < t - 3000:
        self.queue.pop(0)
      
      self.queue.append(t)
    
      return len(self.queue)

obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(4921))
print(obj.ping(5936))
print(obj.ping(5957))

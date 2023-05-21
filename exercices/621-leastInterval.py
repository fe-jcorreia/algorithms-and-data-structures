import heapq

def leastInterval(tasks, n):
  heap = []
  queue = []
  time = 0
  ans = 0

  counter = {}
  for task in tasks: counter[task] = 1 + counter.get(task, 0)
  for key, value in counter.items():
    heapq.heappush(heap, (-value, key))

  while heap or queue:
    if heap:
      val, task = heapq.heappop(heap)
      currVal = -val

      ans += 1
      if currVal > 1:
        queue.append((currVal - 1, task, time + n))
    else:
      ans += 1

    if queue and queue[0][2] == time:
      heapq.heappush(heap, (-queue[0][0], queue[0][1]))
      queue.pop(0)

    time += 1

  return ans


print(leastInterval(["A","A","A","B","B","B"], 2))
print(leastInterval(["A","A","A","B","B","B"], 0))
print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
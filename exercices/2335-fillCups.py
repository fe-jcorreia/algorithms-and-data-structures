import heapq

def fillCups(amount):
  heap = [-q for q in amount]
  heapq.heapify(heap)
  sec = 0

  while heap[0] != 0:
    firstCup = -heapq.heappop(heap)
    secondCup = -heapq.heappop(heap)

    if secondCup == 0:
      heapq.heappush(heap, 0)
    else:
      heapq.heappush(heap, -(secondCup - 1))
    heapq.heappush(heap, -(firstCup - 1))
    sec += 1
  
  return sec


print(fillCups([1,4,2]))
print(fillCups([5,4,4]))
print(fillCups([5,0,0]))

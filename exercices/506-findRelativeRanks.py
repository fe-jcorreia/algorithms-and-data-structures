import heapq

def findRelativeRanks(score):
  award = [num for num in score]
  heap = [num for num in score]
  position = len(award)
  heapq.heapify(heap)

  while heap:
    minItem = heapq.heappop(heap)

    for i, num in enumerate(award):
      if num == minItem:
        if position == 3:
          award[i] = 'Bronze Medal'
        elif position == 2:
          award[i] = 'Silver Medal'
        elif position == 1:
          award[i] = 'Gold Medal'
        else:
          award[i] = str(position)
        break
        
    position -= 1
  
  return award

print(findRelativeRanks([5,4,3,2,1]))
import heapq

def findRelativeRanks(score):
  award = [num for num in score]
  heap = [num for num in score]
  position = len(award)
  heapq.heapify(heap)
  scorePosition = {}

  while heap:
    minItem = heapq.heappop(heap)

    if position == 3:
      scorePosition[minItem] = 'Bronze Medal'
    elif position == 2:
      scorePosition[minItem] = 'Silver Medal'
    elif position == 1:
      scorePosition[minItem] = 'Gold Medal'
    else:
      scorePosition[minItem] = str(position)
        
    position -= 1
  
  for i, num in enumerate(award):
    award[i] = scorePosition[num]

  return award

print(findRelativeRanks([5,4,3,2,1]))
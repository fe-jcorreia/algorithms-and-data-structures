def canCompleteCircuit(gas, cost):
  currTotalGas = 0
  currIndex = 0

  total = 0
  for i in range(len(cost)):
    total += gas[i] - cost[i]
  if total < 0: return -1

  for i in range(len(cost)):
    currTotalGas += gas[i] - cost[i]

    if currTotalGas < 0:
      currTotalGas = 0
      currIndex = i + 1

  return currIndex
    

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(canCompleteCircuit([1,2,3,4,1,9], [3,4,5,1,6,1]))
print(canCompleteCircuit([1,2,3,4,4,1,6], [3,4,5,1,1,6,1]))
print(canCompleteCircuit([2,3,4], [3,4,3]))

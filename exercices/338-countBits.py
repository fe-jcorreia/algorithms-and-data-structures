def countBits_old(n):
  res = []
  count = [0, 1]

  for i in range(n + 1):    

    def countOne(num):
      if num < len(count): return count[num]

      maxPow2 = 1
      while 2**maxPow2 <= num:
        maxPow2 += 1
      maxPow2 -= 1

      oneCount = 1 + countOne(num - 2**maxPow2)
      count.append(oneCount)
      return oneCount

    res.append(countOne(i))
  
  return res

def countBits(n):
  count = [0]
  nextPow2 = 2
  if n == 0: return count
  
  for i in range(1, n + 1):
    if i == nextPow2:
      nextPow2 *= 2
      count.append(1)
      continue
    
    count.append(1 + count[i - (nextPow2 // 2)])

  return count 
  
print(countBits(0))
print(countBits(1))
print(countBits(2))
print(countBits(3))
print(countBits(4))
print(countBits(5))
print(countBits(6))
print(countBits(7))
print(countBits(8))
print(countBits(9))
print(countBits(10))
print(countBits(11))
print(countBits(12))
print(countBits(13))
print(countBits(14))
print(countBits(15))
print(countBits(16))

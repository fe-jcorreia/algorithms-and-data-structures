def addBinary(a, b):
  i, j = len(a) - 1, len(b) - 1
  carry = 0
  ans = []

  while i >= 0 or j >= 0:
    s1 = int(a[i]) if i >= 0 else 0
    s2 = int(b[j]) if j >= 0 else 0
    currSum = s1 + s2 + carry
    
    if currSum > 1:
      carry = 1
      ans.append(str(currSum - 2))
    else: 
      carry = 0
      ans.append(str(currSum))

    i -= 1
    j -= 1
  
  if carry == 1: ans.append("1")

  return "".join(reversed(ans))


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("1011", "1111"))

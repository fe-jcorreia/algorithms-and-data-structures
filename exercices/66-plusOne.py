def plusOne(digits):
  for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
      digits[i] += 1
      break
    
    if i == 0:
      digits[i] = 0
      digits.insert(0, 1)
      break

    digits[i] = 0
  return digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9,9,9,9]))
print(plusOne([1,9,9]))

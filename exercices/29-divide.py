def divide(dividend, divisor):
  if dividend == 0:
    return 0

  INT_MAX = 2**31 - 1
  INT_MIN = -2**31

  sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
  dividend = abs(dividend)
  divisor = abs(divisor)

  quotient = 0
  temp_divisor = divisor
  multiple = 1

  while dividend >= (temp_divisor << 1):
    temp_divisor <<= 1
    multiple <<= 1

  while multiple > 0:
    if dividend >= temp_divisor:
      dividend -= temp_divisor
      quotient += multiple
    temp_divisor >>= 1
    multiple >>= 1

  quotient = sign * quotient
  return min(max(quotient, INT_MIN), INT_MAX)


print(divide(10, 3))
print(divide(7, -3))
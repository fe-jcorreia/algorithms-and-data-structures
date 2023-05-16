def countDigitOne(n):
  ans = 0

  pow10 = 1
  while pow10 <= n:
    divisor = pow10 * 10
    quotient = n // divisor
    remainder = n % divisor

    if quotient > 0:
      ans += quotient * pow10
    if remainder >= pow10:
      ans += min(remainder - pow10 + 1, pow10)
    
    pow10 *= 10

  return ans

# print(countDigitOne(824883294))
# print(countDigitOne(999))
print(countDigitOne(13))
print(countDigitOne(121))
# print(countDigitOne(0))
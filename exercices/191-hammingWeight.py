def hammingWeight(n):
  ans = 0

  for i in range(32):
    ans += (n >> i) & 1

  return ans

print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(4294967293))
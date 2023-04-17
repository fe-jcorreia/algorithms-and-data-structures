def numDecodings_old(s):
  
  def decode(i):
    if i == len(s): return 1
    if s[i] == "0": return 0

    res = decode(i + 1)
    if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
      res += decode(i + 2)
    
    return res

  return decode(0)

def numDecodings(s):
  n = len(s)
  n1, n2 = 1, 0
  
  for i in range(n - 1, -1, -1):
    cur = 0
    if s[i] != "0":
      cur = n1
    if i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"):
      cur += n2

    n2 = n1
    n1 = cur

  return n1 

print(numDecodings("12")) # 2
print(numDecodings("226")) # 3
print(numDecodings("06")) # 0
print(numDecodings("121")) # 3
print(numDecodings("11106")) # 2
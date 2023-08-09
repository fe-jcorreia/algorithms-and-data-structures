def repeatedStringMatch_old(a, b):
  def KMP(haystack, needle, finds):
    n = len(haystack)
    m = len(needle)
    if m > n: return

    lps = [0] * m
    prev, i = 0, 1
    while i < m:
      if needle[i] == needle[prev]:
        lps[i] = prev + 1
        prev += 1
        i += 1
      elif prev == 0:
        lps[i] = 0
        i += 1
      else:
        prev = lps[prev - 1]

    i = j = 0
    while i < n:
      if haystack[i] == needle[j]:
        i, j = i + 1, j + 1
      else:
        if j == 0: i += 1
        else: j = lps[j - 1]
      
      if j == m: 
        finds.append(i - m)
        j = 0

  finds = []
  KMP(a, b, finds)
  if len(finds) > 0: return 1

  finds = []
  KMP(b, a, finds)

  if len(finds) == 0:
    KMP(a + a, b, finds)
    if len(finds) > 0: return 2
    return -1
  
  for i in range(1, len(finds)):
    if finds[i] != finds[i - 1] + len(a):
      return -1

  total = len(finds)
  prefix = b[:finds[0]]
  suffix = b[finds[-1] + len(a):]

  if prefix != "":
    if prefix == a[-len(prefix):]:
      total += 1
    else:
      return -1
  
  if suffix != "":
    if suffix == a[:len(suffix)]:
      total += 1
    else:
      return -1

  return total

def repeatedStringMatch(a, b):
  for i in range(len(b) // len(a) + 3):
    if b in a * i: return i
  return -1


print(repeatedStringMatch("abcd", "cdabcdab"))
print(repeatedStringMatch("abcd", "dab"))
print(repeatedStringMatch("abcd", "cdabcdaxcdabcdab"))
print(repeatedStringMatch("abcd", "cdabcdaxcdab"))
print(repeatedStringMatch("a", "aa"))
print(repeatedStringMatch("aa", "a"))
print(repeatedStringMatch("abc", "cabcabca"))

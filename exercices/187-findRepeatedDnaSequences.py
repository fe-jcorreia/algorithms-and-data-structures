def findRepeatedDnaSequences(s):
  seen = {}
  twice = set()

  for i in range(len(s) - 9):
    if s[i:i + 10] in seen:
      twice.add(s[i:i + 10])
    else:
      seen[s[i:i + 10]] = 1
  
  return twice


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))

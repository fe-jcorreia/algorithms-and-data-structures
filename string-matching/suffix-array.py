def buildSuffixArray(string):
  n = len(string)
  sf = []

  for i in range(n):
    sf.append((i, string[i:n]))

  sf = sorted(sf, key=lambda x: x[1])

  return sf

# print(buildSuffixArray("WERFOSAAABCFABCSEOFDSA"))
# print(buildSuffixArray("WERFOSAAABCFABCSEOFDSA"))
# print(buildSuffixArray("sadbutsad"))
# print(buildSuffixArray("leetcode"))
print(buildSuffixArray("mississippi"))
def preprocess_strong_suffix(shift, bpos, pat, m):
  i = m
  j = m + 1
  bpos[i] = j

  while i > 0:
    while j <= m and pat[i - 1] != pat[j - 1]:
      if shift[j] == 0:
        shift[j] = j - i
      j = bpos[j]

    i -= 1
    j -= 1
    bpos[i] = j

def preprocess_case2(shift, bpos, pat, m):
  j = bpos[0]
  for i in range(m + 1):
    if shift[i] == 0:
      shift[i] = j
    if i == j:
      j = bpos[j]

def search(text, pat):
  s = 0
  m = len(pat)
  n = len(text)
  bpos = [0] * (m + 1)
  shift = [0] * (m + 1)

  preprocess_strong_suffix(shift, bpos, pat, m)
  preprocess_case2(shift, bpos, pat, m)

  while s <= n - m:
    j = m - 1
    while j >= 0 and pat[j] == text[s + j]:
      j -= 1
    if j < 0:
      return s
      # s += shift[0]
    else:
      s += shift[j + 1]


print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("WERFOSAAABCFABCSEOFDSA","AABCFABC"))
print(search("sadbutsad", "sad"))
print(search("leetcode", "leeto"))
print(search("mississippi", "issipi"))
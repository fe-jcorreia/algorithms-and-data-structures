def stringMatching_old(words):
  ans = []
  n = len(words)
  for i in range(n):
    for j in range(n):
      if i == j: continue
      if words[i] in words[j]:
        ans.append(words[i])
        break

  return ans

def stringMatching(words):
  arr = ' '.join(words)
  subStr = [i for i in words if arr.count(i) >= 2]
        
  return subStr

print(stringMatching(["mass","as","hero","superhero"]))
print(stringMatching(["leetcode","et","code"]))
print(stringMatching(["blue","green","bu"]))
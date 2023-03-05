def findJudge(n, trust):
  trusts = {}
  trusted = {}

  for bond in trust:
    trusts[bond[0]] = 1 + trusts.get(bond[0], 0)
    trusted[bond[1]] = 1 + trusted.get(bond[1], 0)

  for i in range(1, n + 1):
    if i not in trusts and trusted.get(i, 0) == n - 1:
      return i
    
  return -1

print(findJudge(2, [[1,2]]))
print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))
print(findJudge(1, []))

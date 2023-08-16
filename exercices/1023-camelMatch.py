def camelMatch(queries, pattern):
  def is_subsequence(query, pattern):
    i, j = 0, 0
    while i < len(query) and j < len(pattern):
      if query[i] == pattern[j]:
        j += 1
      elif query[i].isupper():
        return False
      i += 1
    while i < len(query):
      if query[i].isupper():
        return False
      i += 1
    return j == len(pattern)

  result = []
  for query in queries:
    result.append(is_subsequence(query, pattern))
  return result


print(camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
print(camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"))
print(camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))
print(camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"], "CooP"))

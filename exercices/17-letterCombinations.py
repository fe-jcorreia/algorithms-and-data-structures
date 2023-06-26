def letterCombinations(digits):
    if len(digits) == 0: return []

    decode = {
      "2": ['a', 'b', 'c'],
      "3": ['d', 'e', 'f'],
      "4": ['g', 'h', 'i'],
      "5": ['j', 'k', 'l'],
      "6": ['m', 'n', 'o'],
      "7": ['p', 'q', 'r', 's'],
      "8": ['t', 'u', 'v'],
      "9": ['w', 'x', 'y', 'z']
    }
    ans = []
    currAns = []

    def mapPossibilitites(i):
      if i >= len(digits):
        ans.append("".join(currAns))
        return

      for char in decode[digits[i]]:
        currAns.append(char)
        mapPossibilitites(i + 1)
        currAns.pop()
      
    mapPossibilitites(0)
    return ans


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))

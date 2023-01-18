def isValid(s: str) -> bool:
  stack = []
  complement = {
    ")": "(",
    "]": "[",
    "}": "{"  
  }

  for char in s:
    if char == ']' or char == ')' or char == '}':
      if stack and stack[-1] == complement[char]:
        stack.pop()
      else:
        return False
    else:
      stack.append(char)
  
  if stack:
    return False
  else:
    return True

print(isValid("([)]"))
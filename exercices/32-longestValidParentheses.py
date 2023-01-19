def longestValidParentheses(s: str) -> int:
  stack = [-1]
  maxCharLen = 0

  for i, char in enumerate(s):
    if char == '(':
      stack.append(i)
    else:
      stack.pop()
      if not stack:
        stack.append(i)
      else:
        maxCharLen = max(maxCharLen, i - stack[-1])
  
  return maxCharLen

def longestValidParentheses_opt(s: str) -> int:
  left = right = 0
  maxCharLen = 0

  for char in s:
    if char == '(':
      left += 1
    else:
      right += 1

    if left == right:
      maxCharLen = max(maxCharLen, 2 * right)
    elif right > left:
      left = right = 0

  left = right = 0
  for char in reversed(s):
    if char == '(':
      left += 1
    else:
      right += 1

    if left == right:
      maxCharLen = max(maxCharLen, 2 * left)
    elif left > right:
      left = right = 0

  return maxCharLen

print(longestValidParentheses('(()()')) # 4
print(longestValidParentheses(')((')) # 0
print(longestValidParentheses('()(()')) # 2
print(longestValidParentheses('())((())')) # 4
print(longestValidParentheses(')()())')) # 4

print(longestValidParentheses_opt('(()()')) # 4
print(longestValidParentheses_opt(')((')) # 0
print(longestValidParentheses_opt('()(()')) # 2
print(longestValidParentheses_opt('())((())')) # 4
print(longestValidParentheses_opt(')()())')) # 4

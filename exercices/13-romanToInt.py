def romanToInt(s):
  integerNumber = 0
  lastChar = len(s) - 1

  for i, char in enumerate(s):
    if char == 'I':
      if i < lastChar and (s[i + 1] == 'V' or s[i + 1] == 'X'):
        integerNumber -= 1
      else:
        integerNumber += 1
    
    if char == 'V':
      integerNumber += 5
    
    if char == 'X':
      if i < lastChar and (s[i + 1] == 'L' or s[i + 1] == 'C'):
        integerNumber -= 10
      else:
        integerNumber += 10
    
    if char == 'L':
      integerNumber += 50

    if char == 'C':
      if i < lastChar and (s[i + 1] == 'D' or s[i + 1] == 'M'):
        integerNumber -= 100
      else:
        integerNumber += 100
    
    if char == 'D':
      integerNumber += 500

    if char == 'M':
      integerNumber += 1000
  
  return integerNumber

def romanToInt_opt(s):
  roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }

  integerNumber = 0

  for i in range(len(s) - 1):
    if roman[s[i]] < roman[s[i + 1]]:
      integerNumber -= roman[s[i]]
    else:
      integerNumber += roman[s[i]]
    
  return integerNumber + roman[s[-1]]

print(romanToInt('III')) # 3
print(romanToInt('LVIII')) # 58
print(romanToInt('MCMXCIV')) # 1994

print(romanToInt_opt('III')) # 3
print(romanToInt_opt('LVIII')) # 58
print(romanToInt_opt('MCMXCIV')) # 1994

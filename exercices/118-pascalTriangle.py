def generate(numRows):
  pascal = []
  
  for row in range(numRows):
    line = []
    for col in range(row + 1):
      if col == 0 or col == row:
        line.append(1)
        continue
      line.append(pascal[row - 1][col - 1] + pascal[row - 1][col])
    
    pascal.append(line)

  return pascal

print(generate(5))
print(generate(1))
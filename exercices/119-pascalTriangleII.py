def getRow(rowIndex):
  upperLine = []
  
  for row in range(rowIndex + 1):
    line = []
    for col in range(row + 1):
      if col == 0 or col == row:
        line.append(1)
        continue
      line.append(upperLine[col - 1] + upperLine[col])
    
    upperLine = line

  return upperLine

print(getRow(3))
print(getRow(0))
print(getRow(1))
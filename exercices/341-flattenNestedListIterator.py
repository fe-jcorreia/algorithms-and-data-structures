class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i]

    def hasNext(self) -> bool:
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
            else:
                x = nestedList[i]
                if type(x) == int:
                    return True
                self.stack[-1][1] += 1
                self.stack.append([x, 0])
        return False

# nestedList = [[[[1,2], 1], 2], 3, 4]
nestedList = [[1,1],2,[1,1]]
# nestedList = [1,[4,[6]]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
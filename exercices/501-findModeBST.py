class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def findModeBST(root, seen):
  if not root:
    return
    
  if root.val not in seen:
    seen[root.val] = 1
  else:
    seen[root.val] += 1

  findModeBST(root.left, seen)
  findModeBST(root.right, seen)

def findMode(root):
  seen = {}
  findModeBST(root, seen)

  modeCount = 0
  mode = []
  for item in seen.items():
    if item[1] > modeCount:
      modeCount = item[1]
      mode = [item[0]]
    elif item[1] == modeCount:
      mode.append(item[0])

  return mode


class Solution(object):
  prev = None
  mode = []
  currentCount = 0
  maxCount = 0

  def findMode(self, root):
    self.findModeBST_opt(root)
    return self.mode

  def findModeBST_opt(self, root):
    if not root: 
      return
    
    self.findModeBST_opt(root.left)
    self.currentCount = 1 if root.val != self.prev else self.currentCount + 1
    
    if self.currentCount == self.maxCount:
      self.mode.append(root.val)
    elif self.currentCount > self.maxCount:
      self.mode = [root.val]
      self.maxCount = self.currentCount
    
    self.prev = root.val
    self.findModeBST_opt(root.right)


# tree = TreeNode(1, None, TreeNode(2, TreeNode(2), None))
# tree = TreeNode(0, None, None)
# tree = TreeNode(6, TreeNode(2, TreeNode(2), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
tree = TreeNode(3, TreeNode(2, TreeNode(1, TreeNode(1), None), TreeNode(2)), None)
print(findMode(tree))

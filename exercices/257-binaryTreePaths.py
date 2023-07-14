class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def binaryTreePaths(root):
  ans = []
  currPath = []

  def traverse(root):
    if not root: return
    if not root.left and not root.right:
      currPath.append(str(root.val))
      ans.append("->".join(currPath))
      currPath.pop()
      return
    
    currPath.append(str(root.val))
    traverse(root.left)
    traverse(root.right)
    currPath.pop()
  
  traverse(root)
  return ans
  
tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binaryTreePaths(tree))
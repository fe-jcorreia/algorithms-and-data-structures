class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def twoSumBST(root, k, seen):
  if not root:
    return False
  
  if root.val in seen:
    return True
  else:
    seen[k - root.val] = root.val
  
  return twoSumBST(root.left, k, seen) or twoSumBST(root.right, k, seen)

def findTarget(root, k):
  seen = {}

  return twoSumBST(root, k, seen)

tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
print(findTarget(tree, 9))
print(findTarget(tree, 28))
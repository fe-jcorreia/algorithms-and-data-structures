class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def maxPathSum(root):
  maxSum = float('-inf')

  def search(root):
    nonlocal maxSum
    if not root: return float('-inf')

    left = max(search(root.left), 0)
    right = max(search(root.right), 0)
    maxSum = max(maxSum, root.val + left + right)
    
    return max(root.val + left, root.val + right, root.val)

  search(root)
  return maxSum


tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(), TreeNode(1))))
tree = TreeNode(-3, TreeNode(-2), TreeNode(-1))
tree = TreeNode(2, TreeNode(-1))
tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree = TreeNode(1, TreeNode(2), TreeNode(3))

print(maxPathSum(tree))

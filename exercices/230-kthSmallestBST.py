class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  count = 1
  result = None
  
  def kthSmallestBST(self, root, k):
    if not root:
      return
    
    self.kthSmallestBST(root.left, k)

    if self.count == k:
      self.result = root.val
    
    self.count += 1

    self.kthSmallestBST(root.right, k)


  def kthSmallest(self, root, k):
    self.kthSmallestBST(root, k)
    return self.result
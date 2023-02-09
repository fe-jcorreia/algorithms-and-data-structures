import sys

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    minDiff = sys.maxsize
    prev = None

    def minDiffBST(self, root):
      if not root:
        return self.minDiff

      self.minDiffBST(root.left)
      
      if self.prev != None:
        self.minDiff = min(self.minDiff, root.val - self.prev)
      
      self.prev = root.val

      self.minDiffBST(root.right)

      return self.minDiff

    def minDiffInBST(self, root) -> int:
      return self.minDiffBST(root)

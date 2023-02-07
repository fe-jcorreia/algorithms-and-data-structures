class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

import sys

class Solution:
  minDiff = sys.maxsize
  prev = None

  def getMinimumDifferenceBST(self, root):
    if not root:
      return self.minDiff
    
    self.getMinimumDifferenceBST(root.left)

    if self.prev != None:
      self.minDiff = min(self.minDiff, root.val - self.prev)
    
    self.prev = root.val

    self.getMinimumDifferenceBST(root.right)
    
    return self.minDiff
    
  def getMinimumDifference(self, root):
    return self.getMinimumDifferenceBST(root)


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

import sys

class Solution:
  maxSum = 0
  MAX_INT = sys.maxsize
  MIN_INT = -sys.maxsize - 1
  
  def getMaxSum(self, root):
    if not root:
      return self.MAX_INT, self.MIN_INT, 0
    
    leftMin, leftMax, leftSum = self.getMaxSum(root.left)
    rightMin, rightMax, rightSum = self.getMaxSum(root.right)

    if root.val > leftMax and root.val < rightMin:
      self.maxSum = max(self.maxSum, root.val + leftSum + rightSum)
      return min(root.val, leftMin), max(root.val, rightMax), root.val + leftSum + rightSum

    return self.MIN_INT, self.MAX_INT, 0

  def maxSumBST(self, root):
    self.getMaxSum(root)
    return self.maxSum
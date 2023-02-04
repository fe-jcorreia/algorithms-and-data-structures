import sys
MAX_SIZE = sys.maxsize
MIN_SIZE = -sys.maxsize - 1

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isBST(root, minBound, maxBound):
  if not root:
    return True
  
  if root.val > minBound and root.val < maxBound:
    return isBST(root.left, minBound, root.val) and isBST(root.right, root.val, maxBound)
  
  return False


def isValidBST(root):
  return isBST(root, MIN_SIZE, MAX_SIZE)
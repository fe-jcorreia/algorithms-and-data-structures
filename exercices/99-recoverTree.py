import sys

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  prev = None
  first = None
  second = None

  def inorderTraversalBST(self, root):
    if not root:
      return

    self.inorderTraversalBST(root.left)
    
    if self.prev and root.val < self.prev.val:
      if self.first == None:
        self.first = self.prev
      self.second = root

    self.prev = root 

    self.inorderTraversalBST(root.right)


  def recoverTree(self, root):
    self.inorderTraversalBST(root)

    aux = self.second.val
    self.second.val = self.first.val
    self.first.val = aux

  
def recoverTree_opt(root):
  if not root:
    return

  curr = root
  first = None
  second = None
  prev = None

  while curr != None:
    if curr.left == None:
      if prev and prev.val > curr.val:
        if not first and not second:
          first = prev
          second = curr
        else:
          second = curr

      prev = curr
      curr = curr.right
    else:
      temp = curr.left
      while temp.right and temp.right != curr:
        temp = temp.right
      if not temp.right:
        temp.right = curr
        curr = curr.left
      else:
        if prev and prev.val > curr.val:
          if not first and not second:
            first = prev
            second = curr
          else:
            second = curr
        prev = curr
        temp.right = None
        curr = curr.right
  
  aux = first.val
  first.val = second.val
  second.val = aux

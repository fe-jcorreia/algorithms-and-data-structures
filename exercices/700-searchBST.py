class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def searchBSTHelper(root, val):
  if not root:
    return None
  
  if root.val == val:
    return root

  if val < root.val:
    return searchBSTHelper(root.left, val)
  
  if val > root.val :
    return searchBSTHelper(root.right, val)

def searchBST(root, val):
  return searchBSTHelper(root, val)


def printBST(node, level=0):
  if node != None:
    printBST(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printBST(node.right, level + 1)

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
printBST(searchBST(tree, 2))
printBST(searchBST(tree, 5))
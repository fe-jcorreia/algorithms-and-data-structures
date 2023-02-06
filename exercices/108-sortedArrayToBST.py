class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def placeOnTree(nums, l, r):
  if l > r:
    return None

  mid = (l + r) // 2
  head = TreeNode(nums[mid])

  head.left = placeOnTree(nums, l, mid - 1)

  head.right = placeOnTree(nums, mid + 1, r)

  return head

def sortedArrayToBST(nums):
  return placeOnTree(nums, 0, len(nums) - 1)


def printBST(node, level=0):
  if node != None:
    printBST(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printBST(node.right, level + 1)

printBST(sortedArrayToBST([-10,-3,0,5,9]))

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def generateTrees(n):
  def generate(nums):
    if not nums: return [None]

    ans = []
    for i in range(len(nums)):
      leftTrees = generate(nums[:i])
      rightTrees = generate(nums[i + 1:])

      for l in leftTrees:
        for r in rightTrees:
          root = TreeNode(nums[i])
          root.left = l
          root.right = r
          ans.append(root)
      
    return ans


  nums = [i for i in range(1, n + 1)]
  return generate(nums)


bst = generateTrees(3)
def printBST(node, level=0):
  if node != None:
    printBST(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printBST(node.right, level + 1)

for t in bst:
  printBST(t)
  print("----------------------------------------")
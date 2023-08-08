class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isSubtree_old(root, subRoot):
  def search(r, s):
    if not r and not s: return True
    if (r and not s) or (not r and s): return False

    if r.val == s.val:
      if (search(r.left, s.left)) and search(r.right, s.right):
        return True

    if s == subRoot: 
      return search(r.left, s) or search(r.right, s)
    return False

  return search(root, subRoot)

def isSubtree(root, subRoot):
  strRoot = []
  strSubRoot = []
  
  def getString(r, strR):
    if not r:
      strR.append("#")
      return
    
    strR.append("^")
    strR.append(str(r.val))
    getString(r.left, strR)
    getString(r.right, strR)
  
  getString(root, strRoot)
  getString(subRoot, strSubRoot)

  strRoot = "".join(strRoot)
  strSubRoot = "".join(strSubRoot)

  n = len(strRoot)
  m = len(strSubRoot)
  lps = [0] * m
  prevLPS, i = 0, 1

  while i < m:
    if strSubRoot[i] == strSubRoot[prevLPS]:
      lps[i] = prevLPS + 1
      prevLPS += 1
      i += 1
    elif prevLPS == 0:
      lps[i] = 0
      i += 1
    else:
      prevLPS = lps[prevLPS - 1]
  
  i = j = 0
  while i < n:
    if strRoot[i] == strSubRoot[j]:
      i, j = i + 1, j + 1
    else:
      if j == 0: i += 1
      else: j = lps[j - 1]
    
    if j == m: return True
  
  return False

  

tree1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subTree1 = TreeNode(4, TreeNode(1), TreeNode(2))
tree2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subTree2 = TreeNode(4, TreeNode(1), TreeNode(2))
tree3 = TreeNode(1, TreeNode(1))
subTree3 = TreeNode(1)
tree4 = TreeNode(3, TreeNode(4, TreeNode(1)), TreeNode(5, TreeNode(2)))
subTree4 = TreeNode(3, TreeNode(1), TreeNode(2))
tree5 = TreeNode(1, TreeNode(2), TreeNode(3))
subTree5 = TreeNode(1, TreeNode(2))


print(isSubtree(tree1, subTree1))
print(isSubtree(tree2, subTree2))
print(isSubtree(tree3, subTree3))
print(isSubtree(tree4, subTree4))
print(isSubtree(tree5, subTree5))
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def insertInBST(sortedArray, l, r):
  if l > r:
    return None
  
  mid = (l + r) // 2
  head = TreeNode(sortedArray[mid])
  head.left = insertInBST(sortedArray, l, mid - 1)  
  head.right = insertInBST(sortedArray, mid + 1, r)

  return head


def sortedListToBST(head):
  sortedArray = []
  while head:
    sortedArray.append(head.val)
    head = head.next
  
  return insertInBST(sortedArray, 0, len(sortedArray) - 1)


class Solution:
  solHead = None

  def length(self, head):
    count = 0
    while head != None:
      count += 1
      head = head.next
    return count
    
  def insertBST(self, left, right):
      if left > right: 
        return None
      
      mid = (left + right) // 2
      leftNode = self.insertBST(left, mid - 1)
      
      root = TreeNode(self.solHead.val)
      self.solHead = self.solHead.next
      
      root.left = leftNode
      root.right = self.insertBST(mid + 1, right)
      return root
    
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    self.solHead = head 
    return self.insertBST(0, self.length(self.solHead) - 1)



linkedList = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
tree = sortedListToBST(linkedList)

def printBST(node, level=0):
  if node != None:
    printBST(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printBST(node.right, level + 1)
  
printBST(tree)
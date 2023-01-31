class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def hasCycle(head):
  currentNode = head
  seen = {}

  while currentNode and currentNode.next:
    if currentNode.next in seen:
      return True
    else:
      seen[currentNode.next] = currentNode.next.val

    currentNode = currentNode.next

  return False

def hasCycle_opt(head):
  if not head or not head.next or not head.next.next:
    return False

  hare = head.next.next
  tortoise = head
  
  while hare.next and hare.next.next and tortoise.next:
    if hare == tortoise:
      return True

    hare = hare.next.next
    tortoise = tortoise.next
  
  return False
  
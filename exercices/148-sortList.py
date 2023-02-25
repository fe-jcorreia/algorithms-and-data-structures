class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def sortList(head):
  if not head:
    return
  
  dummy = ListNode(0, head)
  prev, curr = head, head.next

  while curr:
    if curr.val >= prev.val:
      prev, curr = curr, curr.next
      continue
    
    tmp = dummy
    while tmp.next.val < curr.val:
      tmp = tmp.next

    prev.next = curr.next
    curr.next = tmp.next
    tmp.next = curr
    curr = prev.next
  
  return dummy.next

def findMiddle(head):
  tortoise, hare = head, head.next

  while  hare != None and hare.next != None:
    tortoise = tortoise.next
    hare = hare.next.next
  
  return tortoise

def mergeLists(list1, list2):
  tail = dummy = ListNode()
  while list1 and list2:
    if list1.val < list2.val:
      tail.next = list1
      list1 = list1.next
    else:
      tail.next = list2
      list2 = list2.next
    tail = tail.next
  
  if list1:
    tail.next = list1
  if list2:
    tail.next = list2

  return dummy.next

def sortList_opt(head):
  if not head or not head.next:
    return head
  
  left = head
  right = findMiddle(head)
  tmp = right.next
  right.next = None
  right = tmp

  left = sortList_opt(left)
  right = sortList_opt(right)

  return mergeLists(left, right)

# linkedList = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
linkedList = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
# head = sortList(linkedList)
head = sortList_opt(linkedList)
while head != None:
  print(head.val, "-> ", end="")
  head = head.next
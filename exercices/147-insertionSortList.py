class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
      
def insertionSortList(head):
  dummy = ListNode(0, head)
  prev, curr = head, head.next

  while curr:
    if curr.val >= prev.val:
      prev, curr = curr, curr.next
      continue
    
    temp = dummy
    while curr.val > temp.next.val:
      temp = temp.next

    prev.next = curr.next
    curr.next = temp.next
    temp.next = curr
    curr = prev.next
  
  return dummy.next

linkedList = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
# linkedList = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0, None)))))
head = insertionSortList(linkedList)
while head != None:
  print(head.val, "-> ", end="")
  head = head.next
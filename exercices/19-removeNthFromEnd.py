# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  currentNode = head
  deleteNode = head

  while currentNode.next:
    currentNode = currentNode.next
    if n == 0:
      deleteNode = deleteNode.next
    else:
      n -= 1
  
  if n:  
    head = deleteNode.next
  else:
    deleteNode.next = deleteNode.next.next
    
  return head

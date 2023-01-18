# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
      return list2
    if not list2:
      return list1
    
    initialNode = list1 if list1.val <= list2.val else list2
    currentNode = initialNode
    currentArray = initialNode.next
    secondArray = list2 if list1.val <= list2.val else list1

    while currentArray != None or secondArray != None:
      if currentArray == None:
        currentNode.next = secondArray
        break
      if secondArray == None:
        currentNode.next = currentArray
        break

      if secondArray.val <= currentArray.val:
        currentNode.next = secondArray
        secondArray = secondArray.next
        currentNode = currentNode.next
      else:
        currentNode.next = currentArray
        currentArray = currentArray.next
        currentNode = currentNode.next
    
    return initialNode

list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5, None))))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
mergeTwoLists(list1, list2)

curr = list1
while (curr != None):
  print(curr.val)
  curr = curr.next
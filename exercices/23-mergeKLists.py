# Definition for singly-linked list.
from typing import List, Optional

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

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  if not lists:
    return None
  
  resultList = lists[0]

  for i, _ in enumerate(lists):
    if len(lists) - 1 == i:
      break
  
    resultList = mergeTwoLists(resultList, lists[i + 1])
  
  return resultList

def mergeKLists_opt(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  if not lists:
    return None
  
  amount = len(lists)
  interval = 1

  while interval < amount:
    for i in range(0, amount - interval, interval * 2):
      lists[i] = mergeTwoLists(lists[i], lists[i + interval])
    interval *= 2
  
  return lists[0]
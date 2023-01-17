class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
  l1Ptr = l1
  l2Ptr = l2
  carry = 0
  result = ListNode()
  initialNode = result

  while l1Ptr != None or l2Ptr != None or carry != 0:
    l1Val = 0 if not l1Ptr else l1Ptr.val
    l2Val = 0 if not l2Ptr else l2Ptr.val

    listSum = l1Val + l2Val + carry
    carry = listSum // 10
    result.next = ListNode(listSum % 10, None)

    result = result.next
    l1Ptr = None if not l1Ptr else l1Ptr.next
    l2Ptr = None if not l2Ptr else l2Ptr.next

  return initialNode.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode()
        pr = dummy
        carry = 0

        while p1 is not None or p2 is not None or carry != 0:
            v1 = p1.val if p1 is not None else 0
            v2 = p2.val if p2 is not None else 0

            total = v1 + v2 + carry
            carry = total // 10

            pr.next = ListNode(total % 10)
            pr = pr.next

            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next

        return dummy.next

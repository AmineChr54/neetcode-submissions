# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast=head
        slow=head
        m=0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            m += 1
        
        cur = head
        if fast:
            length = m*2 + 1
        else:
            length = m*2

        if length == n:
            return head.next

        for _ in range(length - n):
            tmp = cur
            cur = cur.next
        tmp.next = cur.next
        return head
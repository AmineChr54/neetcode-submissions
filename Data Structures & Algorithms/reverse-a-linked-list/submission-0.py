# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        p = head.next
        prev = head
        head.next = None
        while p != None:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        head = prev
        return head
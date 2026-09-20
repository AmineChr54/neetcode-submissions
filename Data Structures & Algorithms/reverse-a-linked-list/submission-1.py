# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)
        # head.next is currently the tail of the reversed sublist.
        # Make it point back to current head to reverse the link.
        head.next.next = head
        # Disconnect the current head's forward link to prevent cycles
        head.next = None

        return new_head

        
        """if head == None:
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
        
        return head"""
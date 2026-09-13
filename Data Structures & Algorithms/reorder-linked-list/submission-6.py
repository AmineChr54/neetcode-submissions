# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Edge cases
        if not head or not head.next:
            return

        # Count the LinkedList O(N) - O(1)
        count = 0
        c = head
        while c:
            count += 1
            c = c.next

        # Inverse the second half of the Linkedlist O(N) - O(1)
        prev_p2 = head
        for i in range((count - 1) // 2):
            prev_p2 = prev_p2.next

        p2 = prev_p2.next
        prev_p2.next = None

        prev = None
        while p2:
            p2n = p2.next
            p2.next = prev
            prev = p2
            p2 = p2n
            
        # Reorder linked list O(N) - O(1)
        p1, p2 = head, prev

        while p2:
            p1n = p1.next
            p2n = p2.next

            p2.next = p1n
            p1.next = p2

            p2 = p2n
            p1 = p1n
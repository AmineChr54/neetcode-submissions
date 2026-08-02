# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        adresses = set()
        while head:
            adress = id(head)
            if adress in adresses:
                return True
            else:
                adresses.add(id(head))
                head = head.next
        return False
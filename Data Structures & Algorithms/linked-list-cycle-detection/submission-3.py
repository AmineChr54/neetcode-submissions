# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pfast = head
        pslow = head
        
        while pfast and pfast.next:
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow:
                return True
        return False
        
        
        
        
        """adresses = set()
        while head:
            adress = id(head)
            if adress in adresses:
                return True
            else:
                adresses.add(id(head))
                head = head.next
        return False"""
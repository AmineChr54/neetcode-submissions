# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        pfast = head.next
        pslow = head
        while pfast:
            if pfast == pslow:
                return True
            if not pfast.next:
                return False
            pfast = pfast.next.next
            pslow = pslow.next
        return False
        
        
        
        
        adresses = set()
        while head:
            adress = id(head)
            if adress in adresses:
                return True
            else:
                adresses.add(id(head))
                head = head.next
        return False
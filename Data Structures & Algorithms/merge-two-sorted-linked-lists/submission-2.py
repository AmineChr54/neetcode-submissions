# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        p1 = list1
        p2 = list2
        
        result = ListNode()
        if p1.val >= p2.val:
            result.val = p2.val
            p2 = p2.next
        else:
            result.val = p1.val
            p1 = p1.next
        pr=result
        

        while p1 is not None and p2 is not None:
            new_node = ListNode()
            pr.next = new_node
            pr = new_node
            if p1.val >= p2.val:
                pr.val = p2.val
                p2 = p2.next
            else:
                pr.val = p1.val
                p1 = p1.next
        
        if p2 is None:
            pr.next=p1
        if p1 is None:
            pr.next=p2
        
        return result

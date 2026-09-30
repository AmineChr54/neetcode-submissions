"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        
        # deep copy with random=None
        dummy = Node(head.val)
        adresses = {head: dummy}
        cur = dummy
        q = head.next
        while q:
            tmp = Node(q.val)
            cur.next = tmp
            adresses[q] = tmp
            cur = cur.next
            q = q.next
        
        # put randoms
        cur = dummy
        q = head
        while cur: 
            if q.random:
                cur.random = adresses.get(q.random)
            cur = cur.next
            q = q.next

        return dummy
                

            
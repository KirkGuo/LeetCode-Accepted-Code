"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        p = head
        while p:
            q = Node(p.val)
            q.next = p.next
            p.next = q
            p = q.next
        p = head
        while p:
            q = p.next
            q.random = p.random if not p.random else p.random.next
            p = q.next
            if q.next:
                q.next = q.next.next
        return head.next

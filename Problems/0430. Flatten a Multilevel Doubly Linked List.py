"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        return self.flat(head)[0]
    
    def flat(self, head):
        if not head:
            return None, None
        if not head.child and not head.next:
            return head, head
        nxt = head.next
        if head.child:
            front, tail = self.flat(head.child)
            head.next = front
            if front:
                front.prev = head
            if tail:
                tail.next = nxt
            if nxt:
                nxt.prev = tail
            head.child = None
        front, tail = self.flat(nxt)
        return head, tail

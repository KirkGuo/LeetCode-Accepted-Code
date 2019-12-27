# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if head.next == None:
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        for i in range(k%len(l)):
            l = [l[-1]] + l[:-1]
        for idx in range(len(l)):
            l[idx] = ListNode(l[idx])
            if idx:
                l[idx-1].next = l[idx]
        return l[0]
            

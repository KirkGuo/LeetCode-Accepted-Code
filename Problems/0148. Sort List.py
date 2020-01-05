# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ans = self.mergeSort(head)
        return ans
    
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        p_slow = p_fast = head
        p_pre = None
        while p_fast and p_fast.next:
            p_pre = p_slow
            p_fast = p_fast.next.next
            p_slow = p_slow.next
        p_pre.next = None
        
        lst1 = self.mergeSort(head)
        lst2 = self.mergeSort(p_slow)
        
        if not lst1: return lst2
        if not lst2: return lst1
        
        if lst1.val>lst2.val:
            lst1, lst2 = lst2, lst1
        
        p1, p2 = lst1, lst2
        while p1.next and p2:
            if p1.next.val<=p2.val:
                p1 = p1.next
            else:
                tmp1 = p1.next
                tmp2 = p2.next
                p1.next = p2
                p2.next = tmp1
                p2 = tmp2
        if p2:
            p1.next = p2
        
        return lst1

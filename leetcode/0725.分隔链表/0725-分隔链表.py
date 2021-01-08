# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #Ë«Ö¸Õë£¬before£¬after
        p1 = before = ListNode(-1)
        p2 = after = ListNode(-1)
        while head:
            if head.val<x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 =p2.next
            head = head.next
        p2.next = None
        p1.next = after.next
        
        return before.next
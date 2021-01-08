# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dim = ListNode(-1)
        dim.next = head
        p = dim
        for i in range(m-1): #p指向m的前驱
            p = p.next
        cur = p.next
        pre = None
        for i in range(n-m+1):
            cur.next,pre,cur = pre,cur,cur.next
        p.next.next = cur
        p.next = pre
        return dim.next

      
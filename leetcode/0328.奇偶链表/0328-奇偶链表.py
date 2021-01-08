class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def oddEvenList(self,head:ListNode)->ListNode:
        if not head:return head
        odd = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
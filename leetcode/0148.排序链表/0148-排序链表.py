# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        res = ans = ListNode(-1)
        while left and right:
            if left.val<=right.val:
                ans.next = left
                left = left.next
            else:
                ans.next = right
                right = right.next
            ans = ans.next        
        ans.next = left or right
        return res.next
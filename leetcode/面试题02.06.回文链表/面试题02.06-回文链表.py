# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        while slow:
            slow.next,pre,slow  = pre,slow,slow.next
        while pre and head:
            if pre.val!=head.val:return False
            pre = pre.next
            head = head.next
        return True
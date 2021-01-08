# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = []
        p =ans = ListNode(-1)
        while head:
            while head and len(stack)<k:
                stack.append(head)
                head=head.next
            if len(stack)<k:
                p.next = stack[0]
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = None
        return ans.next
            
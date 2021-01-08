# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow=dimmy= ListNode(-1)
        dimmy.next = head
        fast = head        
        while fast and fast.next:
            if slow.next.val !=fast.next.val:
                slow = slow.next
                fast = fast.next
            else:
                while fast and fast.next and slow.next.val==fast.next.val:
                    fast = fast.next
                slow.next=fast.next
                fast=fast.next
            # while head and head.next and p.next.val==head.next.val:
            #     head = head.next
            # if p.next!=head:
            #     p.next = head.next
            # else:
            #     p = head
            # head  = head.next
                    
        return dimmy.next
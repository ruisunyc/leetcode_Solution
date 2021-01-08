# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode: 
        fast = head        
        while fast and fast.next:            
            while fast.next and fast.val==fast.next.val:
                fast.next = fast.next.next
            fast =fast.next
        return head
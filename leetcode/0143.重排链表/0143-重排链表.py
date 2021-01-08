# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            #找到中间节点left为[1,2]
            left=slow =fast=head            
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            #slow.next指向none防止环
            node,slow.next = slow.next, None
            #反转链表后的头结点pre
            pre = None 
            while node:
                node.next,pre,node = pre,node,node.next 
            #交错拼接,左边长度比右边大1或想等                    
            while pre:
                left.next,pre.next,left,pre = pre,left.next,left.next,pre.next
            
        

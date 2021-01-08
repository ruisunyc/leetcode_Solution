"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:return 
        head=tail =None
        def dfs(root): 
            nonlocal head,tail           
            if not root:return             
            dfs(root.left)
            if tail:
                tail.right = root
                root.left = tail
            else:
                head=root
            tail = root
            dfs(root.right)
        dfs(root)  
        tail.right = head      
        head.left = tail        
        return head
        
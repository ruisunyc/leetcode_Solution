# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
            if not t1:return t2
            if not t2:return t1

            q=[[t1,t2]]
            while q:
                i,j = q.pop() 
                i.val+=j.val                
                if i.right and j.right:
                    q.append([i.right,j.right])                 
                if i.left and j.left:
                    q.append([i.left,j.left])
                if not i.right:
                    i.right = j.right
                if not i.left:
                    i.left = j.left                              
            return t1
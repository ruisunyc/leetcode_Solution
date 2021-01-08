# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:return True
        if not s or not t:return False
        return self.issame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    def issame(self,s,t):
        if not s and not t:return True
        if not s or not t:return False
        return s.val ==t.val and self.issame(s.left,t.left) and self.issame(s.right,t.right) 
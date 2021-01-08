# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # if not A and not B:return True
        if not A or not B:return False
        return self.isPartSame(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
    def isPartSame(self,A,B):
        if not B:return True
        if not A:return False
        return A.val==B.val and self.isPartSame(A.left,B.left) and self.isPartSame(A.right,B.right)
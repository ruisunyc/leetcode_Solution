# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:return self.ans
        def dfs(root,mins,maxs):
            if not root:return
            mins = min(root.val,mins)
            maxs = max(root.val,maxs)
            if not root.left and not root.right:
                self.ans = max(self.ans,maxs-mins)
            dfs(root.left,mins,maxs)
            dfs(root.right,mins,maxs)
        dfs(root,root.val,root.val)
        return self.ans
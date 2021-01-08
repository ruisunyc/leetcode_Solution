# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self,root:TreeNode)->int:
        ans = 0
        if not root:return 0
        q = collections.deque([(root,root.val)])
        while q:
            cur,val = q.popleft()
            if not cur.left and not cur.right:ans+=val
            if cur.left:
                q.append((cur.left,val*10+cur.left.val))
            if cur.right:
                q.append((cur.right,val*10+cur.right.val))
        return ans
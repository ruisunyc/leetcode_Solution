# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack,ans = [root],[]
        while stack:
            cur = stack.pop()
            if isinstance(cur,TreeNode):
                stack.extend([cur.right,cur.val,cur.left])
            elif isinstance(cur,int):
                ans.append(cur)
        return ans



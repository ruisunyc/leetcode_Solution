# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        ans = []
        def dfs(tmp,root,cur):
            if not root:return 
            if root.val==cur and not root.left and not root.right:
                tmp+=[root.val]
                ans.append(tmp)
                return
            dfs(tmp+[root.val],root.left,cur-root.val)
            dfs(tmp+[root.val],root.right,cur-root.val)
        dfs([],root,sums)
        return ans
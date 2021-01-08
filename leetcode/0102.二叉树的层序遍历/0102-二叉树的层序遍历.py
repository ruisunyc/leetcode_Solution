# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # ans = []
        # if not root:return ans
        # q = collections.deque([root])
        # while q:
        #     tmp = []
        #     for _ in range(len(q)):
        #         cur = q.popleft()
        #         tmp.append(cur.val)
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        #     ans.append(tmp)
        # return ans
        ans = []
        def dfs(root,depth):
            if not root:return 
            if len(ans)==depth:
                ans.append([])
            ans[depth].append(root.val)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        return ans

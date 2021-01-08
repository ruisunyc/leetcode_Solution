# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(root,par = None):
            if not root:return
            root.parent = par
            dfs(root.left,root)
            dfs(root.right,root)
        dfs(root)
        q = deque([(target,0)])
        tmp = []
        seen = {target}
        while q:
            if q[0][1]==K:
                tmp = [node.val for node,dis in q]   
                break             
            cur,dis = q.popleft()           
            for i in [cur.left,cur.right,cur.parent]:
                if i and i not in seen:
                    seen.add(i)
                    q.append((i,dis+1))               
        return tmp
        

        

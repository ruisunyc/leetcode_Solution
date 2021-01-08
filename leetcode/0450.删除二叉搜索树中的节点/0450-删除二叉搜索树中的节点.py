# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:return 
        if root.val==key:
            if not root.left:return root.right
            if not root.right:return root.left
            right = root.right
            while right.left:
                right = right.left
            right.left = root.left
            return root.right            
        elif root.val>key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root
    
 
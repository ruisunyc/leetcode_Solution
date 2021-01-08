# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # if not root:return 'null'
        # return self.serialize(root.right)+','+self.serialize(root.left)+','+str(root.val)
        q  = deque([root])
        ans=''
        while q:
            node = q.popleft()            
            if node is None:
                ans+='null,'
            else:                
                ans+=str(node.val)+','
                q.append(node.left)
                q.append(node.right)
        return ans[:-1]
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='null':return
        datas = deque(data.split(','))
        root = TreeNode(datas[0])
        i=1
        q = deque([root])
        while q:
            node = q.popleft()
            if datas[i]!='null':
                node.left = TreeNode(datas[i])
                q.append(node.left)
            i+=1            
            if datas[i]!='null':
                node.right = TreeNode(datas[i])
                q.append(node.right)
            i+=1
        return root

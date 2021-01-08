"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.dict = {}
        def dfs(head):
            if not head:return
            if head in self.dict:return self.dict[head]
            node = Node(head.val,None,None)
            self.dict[head] = node
            node.next,node.random = dfs(head.next),dfs(head.random)
            return node
        return dfs(head)

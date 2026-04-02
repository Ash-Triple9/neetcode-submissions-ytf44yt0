# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        The intuition here is that at every particular level,
        the last node at that level is the rightmost node and is the one that will be visible
        So we can do a bfs and only add the nodes that appear at the very end of each level
        '''
        res = []
        queue = collections.deque([])
        if not root:
            return res
        queue.append(root)

        while queue:
            node = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)
        return res
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Given a root
        Have to return a list of lists,
            the list of lists contains int values of the nodes of a tree
            at an increasing level.
        So for doing things level by level, we can implement a breadth first search
        How does a bfs work?
        BFS works using a queue struct, where it will start by queuing up the root node
            then it pops the current node and queues up the neighboring nodes, in this case
            the neighboring nodes are the left and the right child of the current node. 
        We will keep doing this until we have reached the end level. 
        We also need to find a way of keeping track of when the depth changes
        Determine level = 0 at first
        So bfs starts at node 1, queues it up, then while the queue is not empty,
            Determine the number of nodes at current level (len(queue)).
            While the number of nodes have not been dequeued:
                deque the node and enqueue neighboring nodes           
        '''
        res = []
        queue = deque()
        if not root:
            return []
        queue.append(root)
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res


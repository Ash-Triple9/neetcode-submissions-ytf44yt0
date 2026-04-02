# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.res = None
        def dfs(root):
            if not root:
                return 

            dfs(root.left)

            self.n+=1
            if k == self.n:
                self.res = root.val
                return
            print(self.n, root.val)

            dfs(root.right)
        
        dfs(root)
        print(self.res)
        return self.res
        
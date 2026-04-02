# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.rootMap = dict()
        def rootdfs(root):
            if not root:
                return
            if root.val not in self.rootMap:
                self.rootMap[root.val] = []
            self.rootMap[root.val].append(root)
            rootdfs(root.left)
            rootdfs(root.right)

        def dfs(p, q):
            if not p and not q:
                return True
            elif (not p and q) or (p and not q):
                return False
            
            if not p.val == q.val:
                return False
            
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left and right


        rootdfs(root)
        if not subRoot.val in self.rootMap:
            return False
        refList = self.rootMap[subRoot.val]
        flag = False
        for subTreeNode in refList:
            flag = dfs(subTreeNode, subRoot)
            if flag:
                return flag
        return flag

        
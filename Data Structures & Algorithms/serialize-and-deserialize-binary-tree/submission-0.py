# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.retVal = ""
        def dfs(root):
            if not root:
                self.retVal+=",N"
                return
            
            self.retVal+=str(root.val)
            if root.left:
                self.retVal+=","
            dfs(root.left)
            if root.right:
                self.retVal+=","
            dfs(root.right)
        
        dfs(root)
        print(self.retVal)
        return self.retVal

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:      
        lst = data.split(",")
        if lst[0] == '':
            return TreeNode().left
        self.i = 0
        def dfs():
            if lst[self.i]=='N':
                self.i+=1
                return
            root = TreeNode(int(lst[self.i]))
            self.i+=1
            root.left = dfs()
            root.right = dfs()

            return root
        return dfs()

            



        

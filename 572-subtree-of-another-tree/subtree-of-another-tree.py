# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root):
            vals = []
            def dfs(node):
                if not node:
                    vals.append("null")
                    return
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return "." + ".".join(vals) + "."
        
        s1 = serialize(root)
        s2 = serialize(subRoot)
        return s2 in s1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        longest = [0]
        def dfs(node, length):
            if not node:
                longest[0] = max(longest[0], length)
                return
            else:
                dfs(node.left, length+1)
                dfs(node.right, length+1)
                return
        dfs(root, 0)
        return longest[0]
            

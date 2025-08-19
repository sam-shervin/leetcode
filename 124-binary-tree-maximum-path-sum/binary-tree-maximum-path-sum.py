# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.longest = float('-inf')

        def dfs(root):
            if not root:
                return 0
            max_left = max(dfs(root.left), 0)
            max_right = max(dfs(root.right), 0)

            current = max_left+max_right+root.val
            self.longest = max(self.longest, current)

            return root.val+max(max_left, max_right)
        dfs(root)
        return self.longest
            
        
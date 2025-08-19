# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            index = idx_map[root_val]
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            return root

        return helper(0, len(inorder) - 1)    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        if not root:
            return "n"

        q = [root]   # use a simple list
        i = 0

        while i < len(q):   # walk with an index
            node = q[i]
            if node:
                q.append(node.left)
                q.append(node.right)
            i += 1

        # now turn it into a string
        return ",".join(str(node.val) if node else "n" for node in q)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if data == "n":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))

        q = [root]   # again, list + index
        i = 0
        j = 1  # pointer into vals

        while i < len(q) and j < len(vals):
            node = q[i]
            if node:
                # left child
                if vals[j] != "n":
                    node.left = TreeNode(int(vals[j]))
                    q.append(node.left)
                j += 1

                # right child
                if j < len(vals) and vals[j] != "n":
                    node.right = TreeNode(int(vals[j]))
                    q.append(node.right)
                j += 1
            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
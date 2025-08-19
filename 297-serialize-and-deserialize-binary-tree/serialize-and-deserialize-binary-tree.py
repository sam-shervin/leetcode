from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return "n"

        q = [root]
        i = 0

        while i < len(q):
            node = q[i]
            if node:
                q.append(node.left)
                q.append(node.right)
            i += 1

        return ",".join(str(node.val) if node else "n" for node in q)


    def deserialize(self, data):
        if data == "n":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])   # deque instead of list
        j = 1  # pointer into vals

        while q and j < len(vals):
            node = q.popleft()
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

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        queue = [(root, '')]
        while queue:
            node, pre = queue.pop(0)
            if not node.left and not node.right:
                res.append(pre + str(node.val))
                continue
            if node.left:
                queue.append((node.left, pre + str(node.val) + '->'))
            if node.right:
                queue.append((node.right, pre + str(node.val) + '->'))
        return res
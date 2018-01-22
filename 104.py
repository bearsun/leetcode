# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        if root.left:
            maxleft = self.maxDepth(root.left) + 1
        else:
            maxleft = 1
        if root.right:
            maxright = self.maxDepth(root.right) + 1
        else:
            maxright = 1
        return max(maxleft,maxright)
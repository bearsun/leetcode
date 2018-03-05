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

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.count(root)
        
    def count(self, root):
        if not root.left and not root.right:
            return 1
        dleft = 0
        dright = 0
        if root.left:
            dleft = self.count(root.left)
        if root.right:
            dright = self.count(root.right)
        dcur = max(dleft,dright) + 1
        return dcur
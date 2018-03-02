# BFS with queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        queue = [(root.left, root.right)]
        while len(queue) > 0:
            l, r = queue.pop(0)
            if not (l or r):
                continue
            elif not (l and r):
                return False           
            elif l.val != r.val:
                return False
            
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        
        return True
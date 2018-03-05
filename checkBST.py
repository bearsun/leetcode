# Hackerrank: Trees: Is This a Binary Search Tree?
# similar to mergesort
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if not root:
        return True
    b, _, _= checknode(root)
    return b

def checknode(root):
    if not root.left:
        return True, root.data, root.data
    bleft, left_min, left_max = checknode(root.left)
    bright, right_min, right_max = checknode(root.right)
    b = bleft and bright and left_max < root.data and root.data < right_min
    return b, left_min, right_max
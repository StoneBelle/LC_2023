# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        
        # Check if both root are None 
        if p == None and q == None:
            return True
        # Checks if both have root, then compares using recursion
        if p != None and q != None: 
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Checks if one w root and one wo root 
        else:
            return False

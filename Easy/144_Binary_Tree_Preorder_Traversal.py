# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        # Preorder Traversal: visit, left, right
        # check for no root, if None return blank list
        if root == None:
            return []
        # return root value inside a list first
        # use recursion to add L & R children of the root inside its own list
        # recursion will also add L & R grandchildren for the root's children if they are not None

        # concatenate all lists: root, children, grandchildren
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def validate(node: TreeNode | None, low: float, high: float) -> bool:
            # An empty node is a valid BST
            if not node:
                return True
                
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
                
            # Recursively validate the left subtree (values must be less than node.val)
            # and the right subtree (values must be greater than node.val)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
            
        return validate(root, float('-inf'), float('inf'))
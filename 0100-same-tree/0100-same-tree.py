# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Base case 1: If both nodes are None, the subtrees are identical
        if not p and not q:
            return True
            
        # Base case 2: If one node is None and the other is not, or values don't match
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check both the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
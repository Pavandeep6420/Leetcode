# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
            # Both nodes are None -> symmetric
            if not t1 and not t2:
                return True
            # One node is None or their values don't match -> asymmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # Compare outer pair (t1.left, t2.right) and inner pair (t1.right, t2.left)
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right) if root else True
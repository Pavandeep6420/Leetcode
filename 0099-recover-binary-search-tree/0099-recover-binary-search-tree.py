# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node: TreeNode | None):
            if not node:
                return
                
            inorder(node.left)
            
            # Find the nodes where the inorder traversal order is violated
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
                
            self.prev = node
            
            inorder(node.right)
            
        inorder(root)
        
        # Swap the values of the two incorrectly placed nodes back into place
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
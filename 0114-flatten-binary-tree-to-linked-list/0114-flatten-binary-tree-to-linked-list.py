from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Attach original right subtree to the rightmost node of left subtree
                prev.right = curr.right
                
                # Move left subtree to the right and set left to None
                curr.right = curr.left
                curr.left = None
            
            # Move to the next right node
            curr = curr.right
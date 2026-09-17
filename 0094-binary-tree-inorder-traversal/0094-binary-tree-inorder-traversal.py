# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stack = []
        current = root
        
        while current or stack:
            # Step 1: Go as far left as possible, pushing nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
                
            # Step 2: Pop the leftmost node, add its value to the result
            current = stack.pop()
            res.append(current.val)
            
            # Step 3: Move to the right subtree and repeat
            current = current.right
            
        return res
        
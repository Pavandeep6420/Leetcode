from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node: Optional[TreeNode], current_sum: int, path: List[int]):
            if not node:
                return
            
            # Add current node value to path
            path.append(node.val)
            current_sum += node.val
            
            # Check if it's a leaf node and the sum equals targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))
            else:
                # Continue searching left and right subtrees
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
            
            # Backtrack to explore other paths
            path.pop()

        dfs(root, 0, [])
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
            
        memo = {}
        
        def helper(start: int, end: int) -> list[TreeNode | None]:
            if start > end:
                return [None]
                
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            
            # Iterate through all values to use as the root
            for i in range(start, end + 1):
                # Generate all possible left subtrees from numbers less than i
                left_trees = helper(start, i - 1)
                # Generate all possible right subtrees from numbers greater than i
                right_trees = helper(i + 1, end)
                
                # Combine each left and right subtree with the current root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
                        
            memo[(start, end)] = all_trees
            return all_trees
            
        return helper(1, n)
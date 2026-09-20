from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            
            if left > right:
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Build left and right subtrees split by the root index in inorder traversal
            root.left = array_to_tree(left, inorder_map[root_val] - 1)
            root.right = array_to_tree(inorder_map[root_val] + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None

            # The last element in postorder is the root of the current subtree
            root_val = postorder.pop()
            root = TreeNode(root_val)

            idx = inorder_map[root_val]

            # Build right subtree first because postorder visits root last (Left -> Right -> Root)
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)
from typing import Optional

# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        leftmost = root
        
        # Traverse level by level using the `next` pointers established in previous levels
        while leftmost.left:
            curr = leftmost
            while curr:
                # 1. Connect left child -> right child
                curr.left.next = curr.right
                
                # 2. Connect right child -> next node's left child
                if curr.next:
                    curr.right.next = curr.next.left
                
                # Move horizontally across the current level
                curr = curr.next
            
            # Move down to the next level
            leftmost = leftmost.left
            
        return root
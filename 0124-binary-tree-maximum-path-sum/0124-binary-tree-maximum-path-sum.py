class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')
        
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Max path sum from left and right subtrees (ignore negative gains)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price of the new path where the current node is the highest point (split point)
            price_newpath = node.val + left_gain + right_gain
            
            # Update global maximum path sum
            max_sum = max(max_sum, price_newpath)
            
            # For recursion: return maximum contribution this node can give to its parent
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return max_sum
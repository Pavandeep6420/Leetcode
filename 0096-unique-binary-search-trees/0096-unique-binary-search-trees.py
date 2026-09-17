class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [1] * (n + 1)
        
        for i in range(2, n + 1):
            total_trees = 0
            for root in range(1, i + 1):
                # Number of nodes in the left subtree and right subtree
                left = root - 1
                right = i - root
                total_trees += dp[left] * dp[right]
            dp[i] = total_trees
            
        return dp[n]
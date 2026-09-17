class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 1D DP array initialized to 1, representing the first row
        dp = [1] * n
        
        # Iterate through each row starting from the second row
        for _ in range(1, m):
            for j in range(1, n):
                # The number of ways to reach the current cell is the sum of 
                # the ways from the cell above (dp[j]) and the cell to the left (dp[j-1])
                dp[j] += dp[j - 1]
                
        return dp[-1]
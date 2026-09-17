class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize a 1D DP array of size n with all zeros
        dp = [0] * n
        dp[0] = 1  # Starting position
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # If there is an obstacle, no paths can go through here
                    dp[j] = 0
                elif j > 0:
                    # Add paths coming from the left cell
                    dp[j] += dp[j - 1]
                    
        return dp[-1]
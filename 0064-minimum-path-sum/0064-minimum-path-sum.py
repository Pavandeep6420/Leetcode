class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row by accumulating values horizontally
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            
        # Initialize the first column by accumulating values vertically
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        # Compute the minimum path sum for the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        return grid[-1][-1]
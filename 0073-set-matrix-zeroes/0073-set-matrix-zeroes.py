class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_first_col_zero = False
        
        # Step 1: Use the first row and first column as markers
        for i in range(m):
            if matrix[i][0] == 0:
                is_first_col_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step 2: Update inner matrix based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 3: Update the first row if needed
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
                
        # Step 4: Update the first column if needed
        if is_first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
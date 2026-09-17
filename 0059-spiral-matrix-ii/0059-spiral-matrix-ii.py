class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0] * n for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        current = 1
        
        while left < right and top < bottom:
            # 1. Fill top row from left to right
            for i in range(left, right):
                res[top][i] = current
                current += 1
            top += 1
            
            # 2. Fill right column from top to bottom
            for i in range(top, bottom):
                res[i][right - 1] = current
                current += 1
            right -= 1
            
            # 3. Fill bottom row from right to left
            for i in range(right - 1, left - 1, -1):
                res[bottom - 1][i] = current
                current += 1
            bottom -= 1
            
            # 4. Fill left column from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = current
                current += 1
            left += 1
            
        return res  
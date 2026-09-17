class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or greater than the string length, no zigzag pattern is formed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array to store characters for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False
        
        for char in s:
            rows[curr_row] += char
            
            # Change direction when we hit the top or bottom row
            if curr_row == 0:
                going_down = True
            elif curr_row == numRows - 1:
                going_down = False
            
            # Move to the next row up or down
            curr_row += 1 if going_down else -1
            
        # Combine all rows together
        return ''.join(rows)
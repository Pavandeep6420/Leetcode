class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Format representations for rows, columns, and 3x3 boxes
                row_item = (r, val)
                col_item = (val, c)
                box_item = (r // 3, c // 3, val)
                
                if row_item in seen or col_item in seen or box_item in seen:
                    return False
                
                seen.add(row_item)
                seen.add(col_item)
                seen.add(box_item)
                
        return True
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, index: int) -> bool:
            # If we have matched all characters in the word
            if index == len(word):
                return True
            
            # Check bounds, if current cell matches the character, and if it's not visited
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # Temporarily mark the current cell as visited by changing it to a special character
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions (up, down, left, right)
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Restore the cell's original value (Backtracking)
            board[r][c] = temp
            
            return found

        # Iterate through every cell on the board to find a starting point
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                    
        return False
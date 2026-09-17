class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If we've reached the end of both strings, it's a match
            if i >= len(s) and j >= len(p):
                return True
            
            # If pattern is exhausted but string is not, it's not a match
            if j >= len(p):
                return False
            
            # Check if current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # If the next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: Don't use '*' (skip pattern and '*')
                # Option 2: Use '*' (if characters match, move forward in string)
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]
            
            # If no '*', regular match and move forward in both
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return False

        return dfs(0, 0)
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, path: list[int]):
            # If the combination is of size k, add a copy of it to the result
            if len(path) == k:
                result.append(path.copy())
                return
            
            # Iterate through possible numbers from 'start' to 'n'
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop() # Backtrack to explore other possibilities
                
        backtrack(1, [])
        return result
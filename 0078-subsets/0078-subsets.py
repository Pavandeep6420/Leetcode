class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, path: list[int]):
            # Every path represents a valid subset, so we append a copy of it
            result.append(path.copy())
            
            # Iterate through remaining elements to build subsets
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop() # Backtrack to explore other possibilities
                
        backtrack(0, [])
        return result
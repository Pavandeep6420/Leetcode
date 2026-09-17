class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(current_permutation: list[int]):
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            for num in nums:
                if num not in current_permutation:
                    current_permutation.append(num)
                    backtrack(current_permutation)
                    current_permutation.pop()
                    
        backtrack([])
        return result
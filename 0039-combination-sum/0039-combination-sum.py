class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, current_combination: list[int], current_sum: int):
            if current_sum == target:
                result.append(list(current_combination))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                # We can reuse the same element, so we pass 'i' instead of 'i + 1'
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()
                
        backtrack(0, [], 0)
        return result
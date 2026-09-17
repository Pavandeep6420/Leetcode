class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start: int, current_combination: list[int], current_sum: int):
            if current_sum == target:
                result.append(list(current_combination))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicate elements at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                # Since each number can only be used once, we move to i + 1
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()
                
        backtrack(0, [], 0)
        return result
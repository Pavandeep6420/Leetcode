class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        visited = [False] * len(nums)
        
        def backtrack(current_permutation: list[int]):
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            for i in range(len(nums)):
                # If the element is already visited, skip it
                if visited[i]:
                    continue
                
                # If duplicate and the previous identical element was not visited, skip it
                # to avoid generating duplicate permutations
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                current_permutation.append(nums[i])
                backtrack(current_permutation)
                current_permutation.pop()
                visited[i] = False
                
        backtrack([])
        return result
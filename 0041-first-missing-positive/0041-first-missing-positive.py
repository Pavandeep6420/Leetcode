class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Mark numbers out of range [1, n] with a value that won't interfere (e.g., n + 1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
                
        # Step 2: Use index as a hash key by making the value at that index negative
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] = -nums[val - 1]
                    
        # Step 3: Find the first index with a positive value
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        return n + 1
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to check the last index because if we are already 
        # at or beyond the second-to-last index, we don't need another jump.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
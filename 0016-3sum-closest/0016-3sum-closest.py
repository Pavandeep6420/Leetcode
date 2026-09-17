class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            # Optimization: skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find the exact target, return immediately
                if current_sum == target:
                    return target
                
                # Update the closest sum if the current one is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with the target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
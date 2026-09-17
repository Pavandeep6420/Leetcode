class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position of the last unique element
        k = 1
        
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k
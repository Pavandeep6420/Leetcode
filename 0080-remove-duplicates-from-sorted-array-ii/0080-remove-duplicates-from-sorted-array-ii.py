class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for n in nums:
            # Allow the first two elements, or any element that is 
            # different from the element 2 positions before the write pointer
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i
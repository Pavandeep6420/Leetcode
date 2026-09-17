class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for the end of nums1, nums2, and the merged position in nums1
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Merge in reverse order from the back of nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If there are remaining elements in nums2, copy them over
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
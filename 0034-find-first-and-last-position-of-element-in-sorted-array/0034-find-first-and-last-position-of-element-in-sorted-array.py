class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(is_searching_left):
            left, right = 0, len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1  # Look even further left
                    else:
                        left = mid + 1   # Look even further right
                        
            return idx

        left_idx = binary_search(True)
        right_idx = binary_search(False)
        
        return [left_idx, right_idx]
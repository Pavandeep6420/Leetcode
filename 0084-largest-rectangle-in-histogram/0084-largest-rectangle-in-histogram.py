class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stores pairs of (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # Extend the current bar's left boundary backward
            stack.append((start, h))
            
        # Process remaining bars in the stack
        n = len(heights)
        for index, height in stack:
            max_area = max(max_area, height * (n - index))
            
        return max_area
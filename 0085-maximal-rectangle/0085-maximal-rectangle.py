class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        cols = len(matrix[0])
        heights = [0] * cols
        
        for row in matrix:
            # Update the histogram heights for the current row
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Find the largest rectangle for the current row's histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stores pairs of (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
            
        n = len(heights)
        for index, height in stack:
            max_area = max(max_area, height * (n - index))
            
        return max_area
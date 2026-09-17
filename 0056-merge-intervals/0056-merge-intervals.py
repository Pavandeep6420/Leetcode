class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort the intervals based on their starting values
        intervals.sort(key=lambda i: i[0])
        
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            # Get the end of the last added interval in merged
            last_end = merged[-1][1]
            
            # If current interval overlaps with the last one, merge them
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                # Otherwise, add it as a new separate interval
                merged.append([start, end])
                
        return merged
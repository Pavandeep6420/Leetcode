class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        
        for i in range(len(intervals)):
            # If the new interval comes strictly before the current interval, 
            # insert it and return the rest of the array.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # If the current interval comes strictly before the new interval, 
            # append the current interval to the result.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # Otherwise, they overlap, so merge them by updating newInterval.
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                
        # If we loop through everything and haven't inserted yet, append it at the end.
        res.append(newInterval)
        return res